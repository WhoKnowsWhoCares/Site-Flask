from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .forms import LoginForm
from app.models import User


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        logger.info("User authenticated")
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        logger.info(f"User: {user}")
        if user and user.verify_password(form.password.data):
            login_user(user, remember=True)
            flash("Login successful.")
            next = request.args.get("next")
            if not next:
                next = url_for("main.index")
            logger.info(f"Next: {next}")
            flash("Login successful.")
            return redirect(next)
        flash("Invalid email or password.")
        logger.info(f"Login error")
        return redirect(url_for("auth.login"))
    logger.info(f"Login form")
    return render_template("auth/sign-in.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.index"))
