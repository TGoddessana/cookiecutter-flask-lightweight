from cookiecutter_app import settings
from cookiecutter_app.app_factory import create_app

app = create_app(config_object=settings)

if __name__ == "__main__":
    app.run()
