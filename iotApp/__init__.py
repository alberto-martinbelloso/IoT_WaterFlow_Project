from flask import Flask


def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__)
    app.config.from_object('config')

    @app.route('/')
    def hello_world():
        return 'Ca dasa la javanta, que dese le jevente, qui disi li jivinti, co doso lo jovonto UUUUUU UUUUUUUU'

    return app