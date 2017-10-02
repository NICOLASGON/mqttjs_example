#!/usr/bin/python3

import paho.mqtt.client as paho
import random
import json
import time
import sys

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

for line in sys.stdin:
	csv_line = line.split(';')
	point['id'] = 'TrackerTest'
	point['acc']['x'] = csv_line[6]
	point['acc']['y'] = csv_line[7]
	point['acc']['z'] = csv_line[8]
	point['mag']['x'] = csv_line[3]
	point['mag']['y'] = csv_line[4]
	point['mag']['z'] = csv_line[5]
	point['latitude'] = csv_line[0]
	point['longitude'] = csv_line[1]
	point['heading'] = point['mag']['x']
	client1.publish("testing/", json.dumps(point))
