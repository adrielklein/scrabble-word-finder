from flask import Flask


def handle_acknowledge_route():
    return 'OK'


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/acknowledge', '', handle_acknowledge_route)

    return app
