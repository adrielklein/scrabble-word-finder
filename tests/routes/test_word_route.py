import json
from unittest.mock import Mock

from app.finders.word_finder import WordFinder


def test_when_word_route_is_hit_then_returns_words(app, monkeypatch):
    monkeypatch.setattr(WordFinder, 'get_words', Mock(return_value=[]))
    with app.test_client() as test_client:
        response = test_client.get('/words/fakeword')
        assert 200 == response.status_code
        response_string = response.get_data().decode()
        assert [] == json.loads(response_string)['words']


def test_when_requested_word_is_not_alpha_then_server_gives_an_error(app, monkeypatch):
    monkeypatch.setattr(WordFinder, 'get_words', Mock(return_value=[]))
    with app.test_client() as test_client:
        response = test_client.get('/words/h3ll0')
        assert 400 == response.status_code
        response_string = response.get_data().decode()
        assert 'Requested letter string has non-alpha characters' == json.loads(response_string)['errorMessage']


def test_when_letters_are_uppercase_then_then_get_lowercased(app, monkeypatch):
    monkeypatch.setattr(json, 'dumps', Mock(return_value=''))
    mocked_method = Mock()
    monkeypatch.setattr(WordFinder, 'get_words', mocked_method)
    with app.test_client() as test_client:
        test_client.get('/words/Fakeword')
        mocked_method.assert_called_with('fakeword')
