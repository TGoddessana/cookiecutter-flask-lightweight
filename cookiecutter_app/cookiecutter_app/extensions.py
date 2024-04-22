from flask_babel import Babel
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


cors = CORS(resources={r"/api/*": {"origins": "*"}})
debug_toolbar = DebugToolbarExtension()

db = SQLAlchemy(
    session_options={
        "autoflush": False,
        "autocommit": False,
        "expire_on_commit": False
    }
)
migrate = Migrate()
admin = Admin(template_mode="bootstrap4")
babel = Babel()
login_manager = LoginManager()


"""
TODO

flask-smorest
flask-jwt-extended
flask-socketio
"""
