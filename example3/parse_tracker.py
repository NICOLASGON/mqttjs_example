#!/usr/bin/python3

import paho.mqtt.client as paho
import json
import sys

broker="iot.eclipse.org"
port=1883

client1=paho.Client()
client1.connect(broker,port)
client1.loop_start()

for line in sys.stdin:
    try:
        data = json.loads(line)
        client1.publish("testing/", json.dumps(data))
    except:
        pass
