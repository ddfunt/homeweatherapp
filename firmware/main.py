# See https://docs.pycom.io for more information regarding library specifics

from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2
import time
py = Pysense()
mp = MPL3115A2(py,mode=MPL3115A2.ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
si = SI7006A20(py)
lt = LTR329ALS01(py)
li = LIS2HH12(py)

#simple change
print(mp.temperature())
print(mp.temperature())
#print(mp.altitude())
print(si.temperature())
print(si.humidity())
print(lt.light())
while True:
    time.sleep(0.2)
    print(li.acceleration())
while True:
    time.sleep(0.5)
    print('pitch:{}, yaw:{}, roll:{}'.format(li.roll(),
    li.pitch(),
    li.yaw()))


print(py.read_battery_voltage())
