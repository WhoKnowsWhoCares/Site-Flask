from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .forms import LoginForm
from app.models import User
from loguru import logger


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        logger.info(f'Post request to login with email: {form.email.data.lower()}')
        user = User.query.filter_by(email=form.email.data.lower()).first()
        logger.info(f'User found, name: {user.username}')
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            flash('Login successful.')
            return redirect(next)
        flash('Invalid email or password.')
        return redirect(url_for('auth.login'))
    return render_template('auth/sign-in.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

