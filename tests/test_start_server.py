import json
from unittest import mock
from unittest.mock import Mock

import app
from app.main import create_app


def test_when_start_server_script_method_is_run_then_app_starts_serving(monkeypatch):
    mocked_app = Mock()
    monkeypatch.setattr(app.main, 'create_app', Mock(return_value=mocked_app))
    from start_server import start_server
    start_server()

    mocked_app.run.assert_called_with(host='0.0.0.0', port=5000)


def test_when_server_starts_then_load_up_words(app):
    with app.test_client() as test_client:
        response = test_client.get('/words/aht')
        assert 200 == response.status_code
        response_string = response.get_data().decode()
        assert ['at', 'hat'] == json.loads(response_string)['words']
