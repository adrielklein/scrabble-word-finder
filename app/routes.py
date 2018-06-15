import json

from flask import render_template, request


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
        tmp_arr = letter_string.split('|')
        letter_string, pattern = tmp_arr[0], tmp_arr[1]
        is_valid_input = True # letter_string.isalpha()
        status_code = 200 if is_valid_input else 400
        response = {'words': self._word_finder.get_words(letter_string, pattern)} if is_valid_input else {
            'errorMessage': 'Requested letter string has non-alpha characters'}
        return json.dumps(response), status_code


class FrontEndRoute(object):
    path = '/'
    endpoint = 'front_end'

    def handle(self):
        return render_template('layout.html')
