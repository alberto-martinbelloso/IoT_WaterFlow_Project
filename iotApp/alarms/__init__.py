from flask import Blueprint, jsonify

alarms = Blueprint('alarms', __name__)


@alarms.route('/alarms', method=['GET'])
def status():
    return 'hi'
