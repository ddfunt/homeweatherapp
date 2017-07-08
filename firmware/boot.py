import machine
import os
uart = machine.UART(0, 115200)
os.dupterm(uart)

#DO NOT DELETE ABOVE THIS LINE!!!!

from network import WLAN
def connect_wifi():
    wlan = WLAN(mode=WLAN.STA)
    nets = wlan.scan()
    for net in nets:
        if net.ssid == 'dirac2g':
            print('Network found!')
            wlan.connect(net.ssid, auth=(net.sec, 'aaaaaaaa'), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print('WLAN connection succeeded!')
            break
        print('NO NETWORK FOUND!!!')

connect_wifi()
#wlan = WLAN(mode=WLAN.STA)
#wlan.scan()

#wlan.connect(ssid='dirac2g', auth=(WLAN.WPA2, 'aaaaaaaa'))

#while not wlan.isconnected():
#    pass

#print(wlan.ifconfig()) # prints out local IP to allow for easy connection via Pymakr Plugin or FTP Client
