import pytest
from cookiecutter_app.db import db as _db
from cookiecutter_app.settings import TestingConfig
from cookiecutter_app.app_factory import create_app


@pytest.fixture
def app():
    """Create application for the tests."""
    _app = create_app(TestingConfig)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture
def db(app):
    """Create database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def client(app):
    """Create a test client for the tests."""
    return app.test_client()
