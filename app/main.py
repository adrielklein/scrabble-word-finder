from flask import Flask

from app.finders.anagram_finder import AnagramFinder
from app.finders.word_finder import WordFinder
from app.routes import AcknowledgeRoute, WordRoute, FrontEndRoute


def _set_up_routes(routes, app):
    for route in routes:
        app.add_url_rule(route.path, route.endpoint, route.handle)


def _get_words():
    with open('twl06.txt') as f:
        return f.read().split('\n')


def create_app():
    app = Flask(__name__)
    word_finder = WordFinder(AnagramFinder(_get_words()))
    routes = [AcknowledgeRoute(), WordRoute(word_finder), FrontEndRoute()]
    _set_up_routes(routes, app)

    return app
