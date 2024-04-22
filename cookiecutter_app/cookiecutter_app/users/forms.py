from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from cookiecutter_app.users.models import User


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        render_kw={"placeholder": _("Enter your username"), "type": "text"},
        validators=[DataRequired(), Length(min=3, max=80)],
    )
    password = PasswordField(
        "Password",
        render_kw={"placeholder": _("Enter your password")},
        validators=[DataRequired(), Length(min=4, max=80)],
    )

    def validate(self, extra_validators=None):
        super().validate(extra_validators)
        user = User.get_by_username(self.username.data)

        if user is None or not user.check_password(self.password.data):
            self.form_errors.append(_("Invalid username or password"))
            return False

        return True


class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        render_kw={"placeholder": _("Enter your username"), "type": "text"},
        validators=[DataRequired(), Length(min=3, max=80)],
    )
    email = StringField(
        "Email",
        render_kw={"placeholder": _("Enter your email"), "type": "email"},
        validators=[DataRequired(), Email(), Length(min=6, max=80)],
    )
    password1 = PasswordField(
        "Password",
        render_kw={"placeholder": _("Enter your password")},
        validators=[DataRequired(), Length(min=4, max=80)],
    )
    password2 = PasswordField(
        "Password (again)",
        render_kw={"placeholder": _("Re-enter your password")},
        validators=[
            DataRequired(),
            EqualTo("password1", message=_("Passwords must match")),
        ],
    )

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(_("Username already in use."))

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(_("Email already in use."))
