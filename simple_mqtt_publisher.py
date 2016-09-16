#!usr/bin/python
import paho.mqtt.client as mqtt
import time

MAX_VALUE = 30;
MIN_VALUE = 25;
temp = MIN_VALUE;
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.publish("room/temperature/status","Online",1,True)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client('',True,None,mqtt.MQTTv311,"tcp")
client.on_connect = on_connect
client.on_message = on_message

client.connect("172.29.4.96")
client.loop_start()

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

while True:
	time.sleep(10)
	client.publish("room/temperature",temp,1)
	temp+=1
	if(temp>MAX_VALUE):
		temp = MIN_VALUE
