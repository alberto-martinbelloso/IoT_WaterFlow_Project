from influxdb import InfluxDBClient
from flask import Flask, Blueprint
import os

db = Blueprint('Influxdb', __name__)
host = 'localhost'

try:
    if os.environ["DEPLOY"]:
        host = os.environ["INFLUX_HOST"]
except Exception as e:
    print("Running on develop environment")


# client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
client = InfluxDBClient(host=host, port=8086, database='waterflow')


@db.route('/database_status')
def check_database_status():
    return host


def insertPoint(tags, measures, timestamp):
    json_body = [
        {
            "measurement": "flow",
            "tags": tags,
            "time": timestamp,
            "fields": measures
        }
    ]
    client.write_points(json_body)


def getMeasures():
    results = client.query('SELECT * FROM flow LIMIT 100;', database="waterflow")
    points = results.get_points()
    measurements = ""
    for point in points:
        measurements += "%s, %s, %i \n" % (point['time'], point['dev_id'], point["value"])
    return measurements
