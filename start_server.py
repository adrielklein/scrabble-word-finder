from app.main import create_app


def start_server():
    app = create_app()
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    start_server()
