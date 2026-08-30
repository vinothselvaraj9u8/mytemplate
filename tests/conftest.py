import os

import pytest
from sqlalchemy.pool import StaticPool

# ProdConfig reads DATABASE_URL at import time. Ensure tests always have a valid URL.
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")

from appname.settings import TestConfig

# Use an in-memory SQLite DB with a shared connection pool so it works
# reliably on Windows (file-based temp DBs can fail to open due to file locks).
TestConfig.SQLALCHEMY_DATABASE_URI = 'sqlite://'
TestConfig.SQLALCHEMY_ENGINE_OPTIONS = {
    'poolclass': StaticPool,
    'connect_args': {'check_same_thread': False},
}

from appname import create_app
from appname.models import db
from appname.models.user import User


@pytest.fixture()
def testapp(request):
    """Original starter-project fixture: builds a test client and seeds an admin/user pair."""
    app = create_app('appname.settings.TestConfig')
    client = app.test_client()
    db.app = app
    app_ctx = app.app_context()
    app_ctx.push()
    db.create_all()

    if getattr(request.module, "create_user", True):
        admin = User('admin@example.com', 'supersafepassword', admin=True)
        user = User('user@example.com', 'safepassword')
        db.session.add_all([admin, user])
        db.session.commit()

    def teardown():
        db.session.remove()
        db.drop_all()
        app_ctx.pop()

    request.addfinalizer(teardown)
    return client


@pytest.fixture
def app():
    """Create and configure a new app instance for tests that use the `app`/`client` fixtures."""
    app = create_app('appname.settings.TestConfig')

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """A test client for making requests against the app."""
    return app.test_client()
