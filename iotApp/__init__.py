from flask import Flask
from iotApp.database import db
from iotApp.mosquito import mosquito

def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(mosquito)
    app.register_blueprint(db)

    @app.route('/')
    def locoplaya():
        return 'Ca dasa la javanta, que dese le jevente, qui disi li jivinti, co doso lo jovonto UUUUUU UUUUUUUU'

    return app