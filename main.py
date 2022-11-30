# https://stackoverflow.com/questions/43205568/python-flask-server-with-mqtt-subscription

from flask import Flask, render_template, jsonify
import paho.mqtt.client as mqtt
import mosquitto_mqtt_pi
import read_csvfile
from flask_sock import Sock
import random
port = 5000

app = Flask(__name__)
sock = Sock(app)
port = 5000


@app.route('/')
def render_mainpage():
    return render_template('index.html', name="nakyeonko")

# @sock.route('/getSensorData')
# def getSensorData():
#     sensor_data = read_csvfile.read_csv_Sensor_value_last()
#     return jsonify({'sensor_data':sensor_data})

@app.route('/getSensorData')
def getSensorData():
    return jsonify({'sensor_data':random.randint(0, 9)})

if __name__ == '__main__':
    mosquitto_mqtt_pi.mqtt_init()
    app.run(host='0.0.0.0', port=port, debug=True)