from cookiecutter_app.settings import ProductionConfig
from cookiecutter_app.app_factory import create_app

app = create_app(config_object=ProductionConfig)

if __name__ == "__main__":
    app.run()
