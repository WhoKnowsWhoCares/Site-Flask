from flask import render_template
from flask_login import login_required
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')
    
@main.route('/projects')
def projects():
    return render_template('projects.html')

@main.route('/panel')
@login_required
def panel():
    return render_template('panel.html')
