from flask_login import UserMixin
from sqlalchemy.orm import validates
from email_validator import validate_email, EmailNotValidError
from cookiecutter_app.db import Model, TimeStampedMixin
from cookiecutter_app.extensions import db


class User(Model, UserMixin, TimeStampedMixin):
    __tablename__ = "user"

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=True)
    is_active = db.Column(db.Boolean(), default=False)
    is_admin = db.Column(db.Boolean(), default=False)

    @validates("email")
    def validate_email(self, key, email):
        try:
            validate_email(email)
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email: {e}")
        return email

    def __str__(self) -> str:
        return f"<User {self.username}>"
