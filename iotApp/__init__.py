from flask import Flask
from iotApp.database import db
from iotApp.mosquito import mosquito

# create and configure the app

app = Flask(__name__)
app.config.from_pyfile('../config.py')
app.register_blueprint(mosquito)
app.register_blueprint(db)


@app.route("/")
def hello():
    return "Hello World!"