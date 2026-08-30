import pytest
from sqlalchemy.pool import StaticPool

from appname.settings import TestConfig

TestConfig.SQLALCHEMY_DATABASE_URI = 'sqlite://'
TestConfig.SQLALCHEMY_ENGINE_OPTIONS = {
    'poolclass': StaticPool,
    'connect_args': {'check_same_thread': False},
}

from appname import create_app
from appname.models import db as _db


@pytest.fixture
def app():
    """Create and configure a new app instance using an in-memory SQLite DB."""
    app = create_app('appname.settings.TestConfig')

    with app.app_context():
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()


@pytest.fixture
def client(app):
    """A test client for making requests against the app."""
    return app.test_client()
