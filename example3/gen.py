#!/usr/bin/python3

import paho.mqtt.client as paho
import random
import json
import time

broker="iot.eclipse.org"
port=1883

client1=paho.Client()
client1.connect(broker,port)
client1.loop_start()

point = {}
point['acc'] = {}
point['mag'] = {}

while True:
	point['acc']['x'] = random.random() * 40
	point['acc']['y'] = random.random() * 40
	point['acc']['z'] = random.random() * 40
	point['mag']['x'] = random.random() * 40
	point['mag']['y'] = random.random() * 40
	point['mag']['x'] = random.random() * 40
	client1.publish("testing/", json.dumps(point))
	time.sleep(0.1)
