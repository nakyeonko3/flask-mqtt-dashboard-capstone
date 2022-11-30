# https://stackoverflow.com/questions/43205568/python-flask-server-with-mqtt-subscription

from flask import Flask, render_template
import paho.mqtt.client as mqtt
import mosquitto_mqtt_pi
import read_csvfile
from flask_sock import Sock
port = 5000

app = Flask(__name__)
sock = Sock(app)
port = 5000

sensordata = ""

@app.route('/')
def render_mainpage():
    sensor_data = read_csvfile.read_csv_Sensor_value_last()
    return render_template('index.html', data=sensor_data)

@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        sock.send(data)

if __name__ == '__main__':
    mosquitto_mqtt_pi.mqtt_init()
    app.run(host='0.0.0.0', port=port, debug=True)