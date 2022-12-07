import pytest

import manage


@pytest.fixture
def test_client():
    app = manage.app
    return app.test_client()
