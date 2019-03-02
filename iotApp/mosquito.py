from flask import Blueprint, jsonify
from iotApp.database import insertPoint
from iotApp.mongo import get_device
from iotApp.alarms.alarms import post_alarm

import datetime
import ttn
import base64

mosquito = Blueprint('mosquito', __name__)

app_id = "watermeter-test01"
access_key = "ttn-account-v2.S6_w-wpG19AvLeUNjorYMhx4uctru7dmed_fcTwyvlQ"
mqtt_connected = False
last_notification = None


def uplink_callback(msg, client):
    print(" INFO | Received uplink from ", msg.dev_id)

    buff = base64.b64decode(msg.payload_raw)
    sum = 0
    for bytes in buff:
        sum = sum + bytes

    insertPoint(
        {
            'dev_id': msg.dev_id
        },
        {
            "value": sum
        }, msg.metadata.time)

    global last_notification
    last_notification = datetime.datetime.now().timestamp()

    device_info = get_device(msg.dev_id)
    if device_info is None or device_info['threshold'] < 20:
        return
    else:
        print('storing alarm')
        post_alarm(sum,msg.dev_id,msg.metadata.time)


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
