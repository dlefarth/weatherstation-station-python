import Adafruit_BMP.BMP085 as BMP085
import requests
import json
import os
from datetime import datetime

station_id = '5ec6a6c17a5065101cb6d042'
password = '123'
url = "http://130.61.254.198/api/measurements/"
queue_file = 'queue.json'

def measure(): 
    sensor = BMP085.BMP085()
    return {
        'temperature':sensor.read_temperature(), 
        'pressure':sensor_read_pressure()
    }

def read_queue():
    try:
        with open(queue_file, 'r') as file:
            return json.load(file)
    except EnvironmentError:
        return []

def write_queue(queue):
    with open(queue_file, 'w') as file:
        return json.dump(queue, file)

def delete_queue():
    if os.path.exists(queue_file):
        os.remove(queue_file)

queue = read_queue()
measurement = measure()
measurements = queue + [measurement]

res = requests.post(
    url, 
    json = measurements,
    auth = (station_id, password)
)

if res.status_code == requests.codes.ok:
    delete_queue()
else: 
    write_queue(measurements)
