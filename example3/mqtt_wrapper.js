var mqtt;
var reconnectTimeout = 2000;

var host = "iot.eclipse.org";
var port = 80;
var path = "/ws";
var topic = "testing/";

var useTLS = false;
var username = null;
var password = null;
var cleansession = true;

function MQTTconnect() {
	mqtt = new Paho.MQTT.Client(
			host,
			port,
			path,
			"web_" + parseInt(Math.random() * 100, 10)
	);

	var options = {
		timeout: 3,
		useSSL: useTLS,
		cleanSession: cleansession,
		onSuccess: onConnect,
		onFailure: onFailure,
	};

	mqtt.onConnectionLost = onConnectionLost;
	mqtt.onMessageArrived = onMessageArrived;
	mqtt.connect(options);
}

function onConnect() {
	mqtt.subscribe(topic, {qos: 0});
}

function onConnectionLost(response) {
	setTimeout(MQTTconnect, reconnectTimeout);
};

function onFailure(message) {
	setTimeout(MQTTconnect, reconnectTimeout);
}

function onMessageArrived(message) {
	var topic = message.destinationName;
	var payload = JSON.parse(message.payloadString);

	updateInterface(payload);
};
