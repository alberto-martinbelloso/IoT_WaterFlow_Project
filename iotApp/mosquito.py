from flask import Blueprint, jsonify
from iotApp.database import insertPoint
import datetime
import ttn
import base64

mosquito = Blueprint('mosquito', __name__)

app_id = "watermeter-test01"
access_key = "ttn-account-v2.S6_w-wpG19AvLeUNjorYMhx4uctru7dmed_fcTwyvlQ"
mqtt_connected = False
last_notification = None


def uplink_callback(msg, client):
    print("Received uplink from ", msg.dev_id)
    print(msg)

    print("message raw is ", int.from_bytes(base64.b64decode(msg.payload_raw), 'big'))
    insertPoint(
        {
            'dev_id': msg.dev_id
        },
        {
            "value": int.from_bytes(base64.b64decode(msg.payload_raw), 'big')
        }, msg.metadata.time)

    global last_notification
    last_notification = datetime.datetime.now().timestamp()


def connect_callback(res, client):
    print("Connected to the broker :", res)
    print(client)
    global mqtt_connected
    mqtt_connected = res


@mosquito.route('/mosquito_status')
def status():
    return jsonify({
        'connected': mqtt_connected,
        'last_notification': last_notification
    })


handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)

# checking connection
mqtt_client.set_connect_callback(connect_callback)

# connecting to client
mqtt_client.connect()

# Sleep
# time.sleep(120)

#  mqtt_client.close()
