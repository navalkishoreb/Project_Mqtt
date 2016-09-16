#!/usr/bin/python
import time
import serial
import socket
import requests
import sys
import paho.mqtt.client as mqtt

"""usb = serial.Serial(
    port='/dev/ttyACM0',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0)
"""

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0
    )
ser.open()    
newLine = None


def on_connect(client, userdata, flags,resultCode):
	print("Connected with result code "+str(resultCode))
	client.publish("room/temperature/status","online",2,True)

def on_message(client, userdata, messsage):
	print(message.topic+" : "+str(message.payload))



client = mqtt.Client('',True,None,mqtt.MQTTv311,"tcp")
client.on_connect = on_connect
client.on_message = on_message

client.connect("172.29.4.96")
client.loop_start()


def printInHexFormat(binData):
	for ch in binData:
		print '0x%0*X'%(2,ord(ch)),
	print("\n")
	return;

def sendTemperatureToServer(temp):
	r=requests.get("http://api.thingspeak.com/update?key=9W55W474GLEBNBLC&field1="+str(ord(temp)))
	print 'sending...'+ str(r.status_code) +" -- "+ str(r.json())


def publishTemperature(temp):
	client.publish("room/temperature",str(ord(temp)))


while 1:	
	data= ser.readline()
	if(data != '') and (data !="\n") and len(data)==8:
		printInHexFormat(data)
		printInHexFormat(data[-1:])
#		sendTemperatureToServer(data[-1:])
		publishTemperature(data[-1:])
		newLine = True;
	elif(data == '\n'):
	
		print ('\n')			
		
	else:
		if newLine:
			newLine = False;


