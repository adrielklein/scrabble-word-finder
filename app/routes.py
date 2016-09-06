import json


class AcknowledgeRoute(object):
    path = '/acknowledge'
    endpoint = ''

    def handle(self):
        return 'OK'


class WordRoute(object):
    path = '/words/<letter_string>'
    endpoint = 'word'

    def __init__(self, word_finder):
        self._word_finder = word_finder

    def handle(self, letter_string):
        result = {'words': self._word_finder.get_words(letter_string)}
        return json.dumps(result)
