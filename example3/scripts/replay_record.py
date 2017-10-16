#!/usr/bin/python3

import paho.mqtt.client as paho
import json
import sys
import time
from datetime import datetime

if len(sys.argv) < 1:
	print("usage: <filename> [<hour>]")
	sys.exit(1)

if len(sys.argv) == 3:
	first_sample_h=int(sys.argv[2].split(':')[0])
	first_sample_m=int(sys.argv[2].split(':')[1])
	first_sample_s=int(sys.argv[2].split(':')[2])
else:
	first_sample_h=00
	first_sample_m=00
	first_sample_s=00

logfile=sys.argv[1]
broker="archibald.snootlab.info"
port=2522

client1=paho.Client()
client1.connect(broker,port)
client1.loop_start()

start_sending=False
with open(logfile) as f:
	for line in f:
		line = line.strip().split(' ', 1)
		date = datetime.strptime(line[0].split('.')[0], "%Y-%m-%dT%H:%M:%S")

		if date.hour >= first_sample_h and date.minute >= first_sample_m and date.second >= first_sample_s:
			start_sending=True

		if start_sending:
			print(date)
			client1.publish('testing/', line[1])
			time.sleep(0.25)

