from iotApp.mongo import db

col = db['alarms']


def post_alarm(value, device_id, timestamp, threshold):
    alarm = {
        "device_id": device_id,
        "value": value,
        "timestamp": timestamp,
        "threshold": threshold,
        "message": f"Possible leak from device {device_id}. Received value is {value} and threshold {threshold}"
    }
    db['alarms'].insert(alarm)
    return alarm
