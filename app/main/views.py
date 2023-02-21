from flask import render_template, request, flash
from flask_login import login_required
from .forms import SubmitForm
from . import main
import os
import telebot

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')
    
# @main.route('/projects')
# def projects():
#     return render_template('projects.html')

@main.route('/ihome')
def ihome():
    return render_template('ihome.html')

@main.route('/mlsport')
def mlsport():
    return render_template('mlsport.html')

@main.route('/trade4me')
def trade4me():
    return render_template('trade4me.html')

@main.route('/panel')
@login_required
def panel():
    return render_template('panel.html')

@main.route('/telegram', methods=['POST'])
def telegram():
    form = SubmitForm()
    # if form.validate_on_submit():
    name = form.name
    email = form.email
    message = form.message

    # token = os.getenv('TG_API_KEY')
    # url = f"https://api.telegram.org/bot{token}/sendMessage"
    # chat_id=os.getenv('TG_USER_ID')
    # data = {"chat_id": chat_id, "text": f'User {name}, email {email}, sent message: {message}'}
    # requests.post(url, data=data)
    
    bot = telebot.TeleBot(os.getenv('TG_API_KEY'))
    bot.send_message(os.getenv('TG_USER_ID'), f'User {name}, email {email}, sent message: {message}')
    flash('I will contact you soon')
    return render_template('about.html')
