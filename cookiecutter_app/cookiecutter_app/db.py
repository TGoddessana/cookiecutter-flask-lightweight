from .extensions import db


class Model(db.Model):
    """
    Base model, adds "id" as primary key, just like django does.
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


class TimeStampedMixin:
    """
    Mixin that adds created_at and updated_at columns to a derived model.
    """
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
