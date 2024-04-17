from environs import Env
from enum import Enum

env = Env()
env.read_env()


class Environment(str, Enum):
    """
    Environment enum.
    """
    development = "development"
    production = "production"


# Flask envs
ENV = env.str("FLASK_ENV", default=Environment.development)
DEBUG = ENV == Environment.development
SECRET_KEY = env.str("SECRET_KEY", default="SET THE SECRET KEY!!!")

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
