from flask import url_for, request
from cookiecutter_app.users.models import User


def test_login(client, db):
    User.create(username="test", email="test@test.com", password="test123")
    db.session.commit()
    assert User.query.count() == 1

    response = client.post(
        url_for("users.login"),
        data=dict(username="test", password="test123"),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"home" in response.data


def test_register(client, db):
    client.post(
        url_for("users.register"),
        data=dict(
            username="test2",
            email="test2@test.com",
            password1="test123",
            password2="test123",
        ),
        follow_redirects=True,
    )

    assert User.query.filter_by(username="test2").first().username == "test2"
    assert request.path == url_for("home.home")
