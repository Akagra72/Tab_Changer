from machine import Pin
import time
import math
import network
import socket

trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
led = machine.Pin('LED', machine.Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect("your ssid", "your password")
serverAddress = ('Your server private ip', 2222)
bufferSize = 1024
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while wifi.isconnected() == False:
    print('Waiting for Connection....')
    led.value(True)  # turn on the LED
    time.sleep(1)  # wait for one second
    led.value(False)  # turn off the LED
    time.sleep(1)  # wait for one second

led.value(True)
print("Connected..")
wifiInfo = wifi.ifconfig()


def ultra():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = time.ticks_us()
    while echo.value() == 1:
        signalon = time.ticks_us()
    timepassed = signalon - signaloff
    distance = math.floor((timepassed * 0.0343) / 2)
    return distance


while True:
    dis = ultra()
    print(f"The distance from object is {dis} cm")
    time.sleep(1)
    if dis <= 5:
        x = "Changed"
        led.value(False)
        time.sleep(0.1)
        led.value(True)
        clientEncode = x.encode('utf-8')
        UDPClient.sendto(clientEncode, serverAddress)