from cookiecutter_app.settings import ProductionConfig
from cookiecutter_app.app_factory import create_app

from environs import Env

env = Env()
env.read_env()

app = create_app(config_object=env.str("APP_CONFIG_OBJECT", ProductionConfig))

if __name__ == "__main__":
    app.run()
