from unittest import mock

import pytest
from app.main import create_app


@pytest.fixture
def app():
    mocked_open = mock.mock_open(read_data='hat\nat\notherword\n')
    with mock.patch('app.main.open', mocked_open, create=True):
        return create_app()
