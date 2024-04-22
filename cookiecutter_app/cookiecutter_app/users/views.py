from http import HTTPMethod

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user
from cookiecutter_app.db import make_transactional
from cookiecutter_app.users.forms import RegisterForm, LoginForm
from cookiecutter_app.users.models import User
from cookiecutter_app.utils import flash_errors

blueprint = Blueprint("users", __name__)


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.get_by_username(login_form.username.data)
        login_user(user)
        next_url = request.args.get('next')
        return redirect(next_url or url_for('home.home'))
    else:
        flash_errors(login_form, "error")

    return render_template('users/login.html', form=login_form)


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home.home"))


@blueprint.route("/register", methods=[HTTPMethod.GET, HTTPMethod.POST])
@make_transactional
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        user = User.create(
            username=register_form.username.data,
            email=register_form.email.data,
            password=register_form.password1.data,
        )
        flash(f"User {user.username} created", "success")
        return redirect(url_for("home.home"))
    else:
        flash_errors(register_form, "error")

    return render_template("users/register.html", form=register_form)
