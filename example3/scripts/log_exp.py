#!/usr/bin/python3

import paho.mqtt.client as paho
import json
import sys
from datetime import datetime
import signal

broker="localhost"
port=1883
logfile = None

def signal_handler(signal, frame):
	client1.loop_stop()
	logfile.flush()
	logfile.close()
	sys.exit(0)

def on_message(client, userdata, message):
	d = datetime.now()
	logfile.write( datetime.isoformat(datetime.now()) + ' ' + message.payload.decode('utf-8') + '\n' )

signal.signal(signal.SIGINT, signal_handler)

d = datetime.now()
logfile = open( str(d.day) + str(d.month) + str(d.year) + str(d.hour) + str(d.minute) + '.log','w') 

client1=paho.Client()
client1.on_message=on_message
client1.connect(broker,port)
client1.subscribe("testing/")
client1.loop_start()

signal.pause()
