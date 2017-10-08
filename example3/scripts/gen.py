#!/usr/bin/python3

import paho.mqtt.client as paho
import random
import json
import time

offset = -50
amplitude = 120

broker="iot.eclipse.org"
port=1883

client1=paho.Client()
client1.connect(broker,port)
client1.loop_start()

point = {}
point['acc'] = {}
point['mag'] = {}

while True:
	point['acc']['x'] = (random.random() * amplitude) + offset
	point['acc']['y'] = (random.random() * amplitude) + offset
	point['acc']['z'] = (random.random() * amplitude) + offset
	point['mag']['x'] = (random.random() * amplitude) + offset
	point['mag']['y'] = (random.random() * amplitude) + offset
	point['mag']['z'] = (random.random() * amplitude) + offset
	client1.publish("testing/", json.dumps(point))
	time.sleep(0.1)
