# See https://docs.pycom.io for more information regarding library specifics

from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2
import urequests
import time
import json
py = Pysense()
mp = MPL3115A2(py) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
si = SI7006A20(py)
lt = LTR329ALS01(py)
li = LIS2HH12(py)


KEY = 'abcd'
def send_to_server(data):
    data['signature'] = KEY
    payload = json.dumps(data)
    myheaders = {
    "Authorization": "Bearer 38dfbef7900f75cadbae76e33f91363f",
    "Content-Type": "application/json"
    }
    url = 'http://www.myinterestcalc.com/events'#'http://www.myinterestcalc.com/events'
    try:
        x = urequests.urlopen(url, "POST", data=payload, headers=myheaders)
        print('RESPONSE', x.text)
    except Exception:
        print('FAILED SEND')


def get_data():
    resp = {'temp1': mp.temperature(),
            'temp2': si.temperature(),
            'humidity': si.humidity(),
            'light': lt.light(),
            'battery': py.read_battery_voltage(),
            'pressure': mp.pressure()}
    return resp
#simple change
print(mp.temperature())
print(mp.temperature())
#print(mp.altitude())
print(si.temperature())
print(si.humidity())
print(lt.light())


"""
while True:
    time.sleep(0.2)
    print(li.acceleration())
while True:
    time.sleep(0.5)
    print('pitch:{}, yaw:{}, roll:{}'.format(li.roll(),
    li.pitch(),
    li.yaw()))
"""

print(py.read_battery_voltage())
while True:
    data = get_data()
    send_to_server(data)
    time.sleep(1)
