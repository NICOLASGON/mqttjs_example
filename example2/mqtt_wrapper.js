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

var tracker_time_last_message = new Map;
var trackers = new Map;
var drawPaths = true;

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

	d = new Date();
	var timeString = d.getHours().toString() + ':' + d.getMinutes().toString() + ':' + d.getSeconds().toString();
	$('#log_list').prepend('<h6 class="log-title"><b>' + payload.id + ' - ' + timeString + '</b></h6><div class="log-content">' + message.payloadString + '</div>');

	if( trackers.has(payload.id) ) {
		tracker = trackers.get(payload.id);
		if( drawPaths ) {
			L.polyline([tracker.getLatLng(), [payload.latitude, payload.longitude]], {
				weight: 1
			}).addTo(mymap);
		}
		tracker.setRotationAngle(payload.heading);
		tracker.setLatLng([payload.latitude,payload.longitude]);
		tracker_time_last_message.set(payload.id, new Date());
		$('#button-' + payload.id).removeClass("btn-warning btn-danger").addClass("btn-info");
	}
	else {
		tracker = L.marker([payload.latitude, payload.longitude], {icon: aircraftIcon}).addTo(mymap);
		tracker.setRotationOrigin('center center');
		tracker.setRotationAngle(payload.heading);
		tracker.bindPopup(payload.id);
		$('#tracker_list').append('<button type="button" onclick="zoomToTracker(\'' + payload.id + '\')" id="button-' + payload.id + '" class="btn btn-info">' + payload.id + '</button>');
		trackers.set(payload.id, tracker);
		tracker_time_last_message.set(payload.id, new Date());
	}
};
