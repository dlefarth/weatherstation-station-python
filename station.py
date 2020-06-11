import Adafruit_BMP.BMP085 as BMP085
import requests

stationId = '5ec6a6c17a5065101cb6d042'
passowrd = '123'
url = "localhost:8080/api/measurements/$stationId"

sensor = BMP085.BMP085()

measurement = {'temperature':sensor.read_temperature(), 'pressure':sensor_read_pressure()}

res = requests.post(url, data = measurement, auth=(stationId, password))

if res.status_code == requests.codes.ok:

    else

def read_queue():


def write_queue():
