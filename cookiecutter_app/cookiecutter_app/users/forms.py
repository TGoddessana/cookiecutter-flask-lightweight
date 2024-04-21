from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from cookiecutter_app.users.models import User


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        render_kw={"placeholder": "Username", "type": "text"},
        validators=[DataRequired(), Length(min=3, max=80)],
    )
    password = PasswordField(
        "Password",
        render_kw={"placeholder": "Password"},
        validators=[DataRequired(), Length(min=4, max=80)],
    )


class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        render_kw={"placeholder": "Username", "type": "text"},
        validators=[DataRequired(), Length(min=3, max=80)],
    )
    email = StringField(
        "Email",
        render_kw={"placeholder": "Email", "type": "email"},
        validators=[DataRequired(), Email(), Length(min=6, max=80)],
    )
    password1 = PasswordField(
        "Password",
        render_kw={"placeholder": "Password"},
        validators=[DataRequired(), Length(min=4, max=80)],
    )
    password2 = PasswordField(
        "Verify password",
        render_kw={"placeholder": "Verify password"},
        validators=[
            DataRequired(),
            EqualTo("password1", message="Passwords must match"),
        ],
    )

    # TODO : ADD i18n
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use.")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already in use.")
