import pytest
from app.main import create_app


@pytest.fixture
def app():
    return create_app()
