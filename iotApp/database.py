from influxdb import InfluxDBClient


# client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)

def connect_to_database():
    client = InfluxDBClient(host='localhost', port=8086)
    results = client.query('SELECT * FROM flow;', database="waterflow")
    points = results.get_points()
    measurements = ""
    for point in points:
        measurements += "%s, %s, %i \n" % (point['time'], point['devid'], point["value"])
    return measurements
