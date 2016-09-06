from flask import Flask

from app.anagram_finder import AnagramFinder
from app.routes import AcknowledgeRoute, WordRoute
from app.word_finder import WordFinder


def _set_up_routes(routes, app):
    for route in routes:
        app.add_url_rule(route.path, route.endpoint, route.handle)


def create_app():
    app = Flask(__name__)
    word_finder = WordFinder(AnagramFinder([]))
    routes = [AcknowledgeRoute(), WordRoute(word_finder)]
    _set_up_routes(routes, app)

    return app
