import os

from app.main import create_app

PORT = 5000


def start_server():
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', PORT)))


if __name__ == '__main__':
    start_server()
