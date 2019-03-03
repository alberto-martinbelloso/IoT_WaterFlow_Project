from iotApp.mongo import db

if 'alarms' not in db.collection_names():
    db.create_collection('alarms')

col = db['alarms']


def post_alarm(value, device_id, timestamp, threshold):
    alarm = {
        "device_id": device_id,
        "value": value,
        "timestamp": timestamp,
        "threshold": threshold,
        "message": f"Possible leak from device {device_id}. Received value is {value} and threshold {threshold}"
    }
    col.insert(alarm)
    return alarm
