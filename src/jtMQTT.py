#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")

def pubMsg(topic, payload):
    print('Trying to publish')
    publish.single(topic, payload,client_id = 'rpi')

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(client_id = 'rpi')
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.10", 1883, 60)

pubMsg('/streamDeck/test/','{"action":"test","subject":"alsoTest"}')

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()