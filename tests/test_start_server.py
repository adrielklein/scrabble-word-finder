from unittest.mock import Mock

import app.main



def test_when_start_server_script_method_is_run_then_app_starts_serving(monkeypatch):
    mocked_app = Mock()
    monkeypatch.setattr(app.main, 'create_app', Mock(return_value=mocked_app))
    from start_server import start_server
    start_server()

    mocked_app.run.assert_called_with(host='0.0.0.0', port=5000)
