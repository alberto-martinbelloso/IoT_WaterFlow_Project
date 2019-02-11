from influxdb import InfluxDBClient
from flask import Flask, Blueprint

db = Blueprint('Influxdb', __name__)


# client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
client = InfluxDBClient(host='localhost', port=8086)


@db.route('/database_status')
def check_database_status():
    return getMeasures()


def getMeasures():
    results = client.query('SELECT * FROM flow LIMIT 100;', database="waterflow")
    points = results.get_points()
    measurements = ""
    for point in points:
        measurements += "%s, %s, %i \n" % (point['time'], point['devid'], point["value"])
    return measurements
