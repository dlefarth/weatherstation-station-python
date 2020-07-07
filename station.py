import Adafruit_BMP.BMP085 as BMP085
import requests
import json
import os
from datetime import datetime
import time
from timeloop import Timeloop
from datetime import timedelta

timeloop = Timeloop()

station_id = '5ec6a6c17a5065101cb6d042'
password = '123'
url = "http://130.61.254.198/api/measurements/"
queue_file = 'queue.json'

def measure(): 
    sensor = BMP085.BMP085()
    return {
        'temperature':sensor.read_temperature(), 
        'pressure':sensor.read_pressure(),
        'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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

def run():
    queue = read_queue()
    measurement = measure()
    measurements = queue + [measurement]

    print(measurements)
    
    try:
        res = requests.post(
            url, 
            json = measurements,
            auth = (station_id, password)
        )

        if res.status_code == requests.codes.ok:
            print('sent to server, deleting queue')
            delete_queue()
        else: 
            raise Exception('Not successful')
    except:
            write_queue(measurements)
            print('sending to server failed, saving in queue')
while True:
    run()
    time.sleep(6000)

