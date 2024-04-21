from http import HTTPMethod

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user
from cookiecutter_app.db import make_transactional
from cookiecutter_app.users.forms import RegisterForm, LoginForm
from cookiecutter_app.users.models import User

blueprint = Blueprint("users", __name__)


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if request.method == "POST":
        if login_form.validate_on_submit():
            user = User.query.filter_by(username=login_form.username.data).first()
            if user and user.check_password(login_form.password.data):
                login_user(user)
                return redirect(url_for("home.home"))
            else:
                flash("Invalid username or password", "error")
        else:
            flash("Form is not valid", "error")

    return render_template("users/login.html", form=login_form)


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
        for field, field_errors in register_form.errors.items():
            for error in field_errors:
                flash(f"{field}: {error}", "error")

    return render_template("users/register.html", form=register_form)
