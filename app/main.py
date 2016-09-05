import json

from flask import Flask

from app.anagram_finder import AnagramFinder
from app.word_finder import WordFinder


def handle_acknowledge_route():
    return 'OK'


def handle_word_route(letter_string):
    anagram_finder = AnagramFinder([])
    word_finder = WordFinder(anagram_finder)
    result = {'words': word_finder.get_words(letter_string)}
    return json.dumps(result)


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/acknowledge', '', handle_acknowledge_route)
    app.add_url_rule('/words/<letter_string>', 'word', handle_word_route)

    return app
