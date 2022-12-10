# https://stackoverflow.com/questions/43205568/python-flask-server-with-mqtt-subscription

from flask import Flask, render_template, jsonify
import paho.mqtt.client as mqtt
from mosquitto_mqtt_class import Mqtt_class
import read_csvfile
import random
from bmp_sensor import start_bmp_sensor

port = 5000

app = Flask(__name__)
port = 5000
sensor_value = 0

@app.route('/')
def render_mainpage():
    return render_template('index.html', name="nakyeonko")

@app.route('/getSensorData')
def getSensorData():
    temper_sensor_value = float(read_csvfile.get_senor_data_last_value())
    return jsonify({'sensor_data':temper_sensor_value})

@app.route('/getPHSensorData')
def getPHSensorData():
    sensor_value = float(read_csvfile.get_senor_data_last_value())
    return jsonify({'sensor_data':sensor_value})

@app.route('/turnOn')
def turnOn():
    mqtt_test.turnOn()
    return "1"

@app.route('/turnOff')
def turnOff():
    mqtt_test.turnOff()
    return "0"

if __name__ == '__main__':
    mqtt_test = Mqtt_class()
    mqtt_test.init()
    start_bmp_sensor()
    app.run(host='0.0.0.0', port=port, debug=True)