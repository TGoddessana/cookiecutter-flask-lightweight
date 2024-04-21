from functools import wraps

from .extensions import db


class Transactional:
    def __call__(self, func):
        """
        Decorator that wraps a function in a transaction.
        if an exception is raised, the transaction will be rolled back.
        """

        @wraps(func)
        def _transactional(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
            return result

        return _transactional


class ActiveRecordMixin:
    """
    Mixin that adds CRUD operations to a derived model.

    Note that we don't call db.session.commit() here,
    so the caller is responsible for that.
    """

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        return instance

    @classmethod
    def list(cls, page=1, per_page=10, order_by=None, **kwargs):
        query = cls.query.filter_by(**kwargs)

        if order_by is not None:
            for order in order_by:
                query = query.order_by(order)

        pagination = query.paginate(page, per_page, error_out=False)
        return pagination

    @classmethod
    def get_by_id(cls, id):
        """
        we only provide a get method for the primary key.
        """
        return cls.query.get(id)

    @classmethod
    def update(cls, id, **kwargs):
        instance = cls.query.get(id)

        for key, value in kwargs.items():
            setattr(instance, key, value)

        return instance

    @classmethod
    def delete(cls, id):
        instance = cls.query.get(id)
        db.session.delete(instance)


class Model(db.Model, ActiveRecordMixin):
    """
    Base model, adds "id" as primary key, just like django does.
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TimeStampedMixin:
    """
    Mixin that adds created_at and updated_at columns to a derived model.
    """

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
