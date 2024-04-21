from flask import Flask

from .extensions import cors, db, debug_toolbar, migrate, login_manager
from .home.views import blueprint as home_blueprint
from .users.views import blueprint as users_blueprint


def create_app(config_object):
    app = Flask("cookiecutter_app")
    app.config.from_object(config_object)

    _register_extensions(app)
    _register_blueprints(app)
    _register_error_handlers(app)
    _register_shell_context(app)
    _register_commands(app)
    _configure_logger(app)

    return app


def _register_extensions(app):
    cors.init_app(app)
    db.init_app(app)
    _import_models()
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)
    login_manager.init_app(app)
    _setup_login_manager()


def _import_models():
    from .users import models  # noqa: F401


def _setup_login_manager():
    @login_manager.user_loader
    def load_user(user_id):
        from .users.models import User

        user = User.query.get(user_id)
        return user


def _register_blueprints(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(users_blueprint)


def _register_error_handlers(app):
    pass


def _register_shell_context(app):
    pass


def _register_commands(app):
    pass


def _configure_logger(app):
    pass
