from flask import redirect, render_template, url_for, request, flash
from flask_login import login_required
from .forms import MessageForm
from . import main
import os
import telebot

bot = telebot.TeleBot(os.getenv('TG_API_KEY'))

@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/about')
# def about():
#     return render_template('about.html')
    
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


@main.route('/about', methods=['GET', 'POST'])
def about():
    form = MessageForm()
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
        message = form.message.data
        bot.send_message(os.getenv('TG_USER_ID'), f'User {name}, email {email}, sent message: {message}')
        return redirect(url_for('main.about'))
    return render_template('about.html', form=form)