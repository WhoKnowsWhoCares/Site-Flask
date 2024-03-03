import os
import telebot
import requests

from flask import redirect, render_template, url_for, request, send_from_directory
from flask_login import login_required
from loguru import logger

from .forms import MessageForm
from . import main


bot = telebot.TeleBot(os.getenv("TG_API_KEY", ""))


def if_url_exist(url):
    try:
        request = requests.get(url)
        logger.info(f"Checking if url exist {url}: {request.status_code}")
        return request.status_code == requests.codes.ok
    except Exception as e:
        logger.info(f"Error while checking if url exist {e}")
        return False


@main.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")


@main.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml")


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/ihome")
def ihome():
    return render_template("ihome.html")


@main.route("/mlsport")
def mlsport():
    return render_template("mlsport.html")


@main.route("/trade4me")
def trade4me():
    return render_template("trade4me.html")


@main.route("/panel")
@login_required
def panel():
    return render_template("panel.html")


@main.route("/sd_art")
def sd_art():
    return render_template("sd_art.html")


@main.route("/about", methods=["GET", "POST"])
def about():
    form = MessageForm()
    if request.method == "POST":
        name = form.name.data
        email = form.email.data
        message = form.message.data
        bot.send_message(
            os.getenv("TG_USER_ID", ""),
            f"User {name}, email {email}, sent message: {message}",
        )
        return redirect(url_for("main.about"))
    return render_template("about.html", form=form)


@main.route("/textsummary", methods=["GET", "POST"])
def textsummary():
    textsummary_service = "http://10.0.0.6:6001/"
    if if_url_exist(textsummary_service):
        logger.info("Text summary service is available")
        return render_template("textsummary.html", iframe=textsummary_service)
    else:
        logger.info("Text summary service is unavailable")
        return render_template("/errors/error.html", message="Service is not available")


@main.route("/newsparser")
def newsparser():
    return render_template("newsparser.html")


@main.route("/mltoolsbot")
def mltoolsbot():
    return render_template("mltoolsbot.html")
