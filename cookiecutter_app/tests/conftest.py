import pytest
from cookiecutter_app.db import db as _db
from cookiecutter_app.settings import TestingConfig
from cookiecutter_app.app_factory import create_app
from cookiecutter_app.users.models import User


@pytest.fixture(scope="session")
def app():
    """Create application for the tests."""
    _app = create_app(TestingConfig)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture(scope="function")
def db(app):
    """Create database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    """Create a test client for the tests."""
    return app.test_client()


@pytest.fixture(scope="function")
def user(db):
    """Create a user for the tests."""

    user = User(username="test", email="test@test.com", password="test123")
    db.session.add(user)
    db.session.commit()

    return user
