from flask import Flask, render_template, request

from .admin.views import AdminIndexView, ModelView
from .cli import translate
from .extensions import cors, db, debug_toolbar, migrate, login_manager, admin, babel
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
    _import_models()

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)

    login_manager.init_app(app)
    _setup_login_manager()

    admin.init_app(app, index_view=AdminIndexView())
    _setup_admin(admin)

    babel.init_app(app, locale_selector=_get_locale, timezone_selector=_get_timezone)


def _import_models():
    # import your models,
    # so that Flask-Migrate can detect them

    from .users import models  # noqa: F401


def _setup_login_manager():
    login_manager.login_view = "users.login"

    @login_manager.user_loader
    def load_user(user_id):
        from .users.models import User

        user = User.query.get(user_id)
        return user


def _setup_admin(_admin):
    from .users.models import User

    _admin.name = "cookiecutter_app Admin"
    _admin.add_view(ModelView(User, db.session))


def _get_locale():
    return request.accept_languages.best_match(['en', 'ko'])


def _get_timezone():
    return "UTC"


def _register_blueprints(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(users_blueprint)


def _register_error_handlers(app):
    def render_error(error):
        error_code = getattr(error, "code", 500)
        return render_template(f"error_{error_code}.html"), error_code

    for errcode in [401, 403, 404, 500]:
        app.errorhandler(errcode)(render_error)


def _register_shell_context(app):
    pass


def _register_commands(app):
    app.cli.add_command(translate)


def _configure_logger(app):
    pass
