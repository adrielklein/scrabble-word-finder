import json
from unittest.mock import Mock

from app.word_finder import WordFinder


def test_when_word_route_is_hit_then_returns_words(app, monkeypatch):
    monkeypatch.setattr(WordFinder, 'get_words', Mock(return_value=[]))
    with app.test_client() as test_client:
        response = test_client.get('/words/fakeword')
        assert 200 == response.status_code
        response_string = response.get_data().decode()
        assert [] == json.loads(response_string)['words']
