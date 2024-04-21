from flask_login import UserMixin
from sqlalchemy.orm import validates
from email_validator import validate_email, EmailNotValidError
from werkzeug.security import generate_password_hash, check_password_hash

from cookiecutter_app.db import Model, TimeStampedMixin
from cookiecutter_app.extensions import db


class User(Model, UserMixin, TimeStampedMixin):
    __tablename__ = "user"

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)

    @validates("username")
    def validate_username(self, key, username):
        if User.query.filter(User.username == username).first():
            raise ValueError("Username already in use")

        return username

    @validates("email")
    def validate_email(self, key, email):
        try:
            validate_email(email)
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email: {e}")
        return email

    @classmethod
    def create(cls, **kwargs):
        """
        Create a new user instance and set the hashed password.
        """
        instance = cls(**kwargs)
        instance._set_password(kwargs["password"])
        db.session.add(instance)
        return instance

    def _set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)

    def __str__(self) -> str:
        return f"<User {self.username}>"
