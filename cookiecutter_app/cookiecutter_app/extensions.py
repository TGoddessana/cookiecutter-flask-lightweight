from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

cors = CORS(resources={r"/api/*": {"origins": "*"}})
debug_toolbar = DebugToolbarExtension()

db = SQLAlchemy()
migrate = Migrate()

"""
TODO

flask-login
flask-admin
flask-smorest
flask-socketio
"""