from flask import current_app, request, url_for, redirect
from flask_admin import expose, AdminIndexView as _AdminIndexView
from flask_admin.contrib.sqla import ModelView as _ModelView
from flask_login import current_user, login_required


class AdminIndexView(_AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        config_values = {key: str(value) for key, value in current_app.config.items()}

        return self.render(
            'admin/index.html',
            config_values=config_values,

        )


class ModelView(_ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
