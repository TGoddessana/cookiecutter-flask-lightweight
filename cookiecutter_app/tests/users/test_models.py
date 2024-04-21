import pytest

from cookiecutter_app.users.models import User


def test_user_creation(db) -> None:
    user = User.create(username='test', email='test@test.com', password='test123')
    db.session.commit()

    assert User.query.count() == 1
    assert user.username == 'test'
    assert user.email == 'test@test.com'
    assert user.check_password('test123')


def test_username_validation(db) -> None:
    User.create(username='test', email='test1@test.com', password='test123')
    db.session.commit()

    with pytest.raises(ValueError):
        User.create(username='test', email='test2@test.com', password='test123')

    assert User.query.count() == 1


def test_email_validation(db) -> None:
    User.create(username='test', email='test@test.com', password='test123')
    db.session.commit()

    with pytest.raises(ValueError):
        User.create(username='test2', email='invalid_email', password='test123')

    assert User.query.count() == 1


def test_password_hashed(db) -> None:
    user = User.create(username='test', email="test@test.com", password="test123")
    db.session.commit()

    assert User.query.count() == 1
    assert user.password is not "test123"


def test_password_check(db) -> None:
    user = User.create(username='test', email='test@test.com', password='test123')
    db.session.commit()

    assert User.query.count() == 1
    assert user.check_password('test123')
    assert not user.check_password('wrong_password')
