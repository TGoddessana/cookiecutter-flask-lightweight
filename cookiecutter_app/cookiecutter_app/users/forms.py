from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupForm(FlaskForm):
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
