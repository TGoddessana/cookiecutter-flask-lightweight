from environs import Env
from enum import Enum

from flask import Config

env = Env()
env.read_env()


class Environment(str, Enum):
    """
    Environment enum.
    """

    development = "development"
    production = "production"


class BaseConfig(Config):
    """
    Base configuration.
    """

    # Flask envs
    SECRET_KEY = env.str("SECRET_KEY", default="SET THE SECRET KEY!!!")

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Admin
    FLASK_ADMIN_SWATCH = "flatly"

    # Flask-Babel
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_TRANSLATION_DIRECTORIES = "../translations"
    LANGUAGES = {
        "en": "English",
        "ko": "Korean",
        # Add more languages here...
    }


class ProductionConfig(BaseConfig):
    ENV = Environment.production
    DEBUG = False
    DEBUG_TB_ENABLED = False


class DevelopmentConfig(BaseConfig):
    ENV = Environment.development
    DEBUG = True

    # Flask-Debug-Toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    ENV = Environment.development
    DEBUG = True
    TESTING = True

    WTF_CSRF_ENABLED = False  # Allows form testing
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
