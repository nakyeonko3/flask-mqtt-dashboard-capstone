# https://stackoverflow.com/questions/43205568/python-flask-server-with-mqtt-subscription

from flask import Flask, render_template, jsonify
import paho.mqtt.client as mqtt
from mosquitto_mqtt_class import Mqtt_class
import read_csvfile
import random
from temper_sensor import start_bmp_sensor
from temper_sensor_minutes import start_bmp_sensor_minutes
from servo import Auto_servo_Thread, servo_motor_control

auto_servo = Auto_servo_Thread()
port = 5000

app = Flask(__name__)
port = 5000
sensor_value = 0

@app.route('/')
def render_mainpage():
    return render_template('index.html', name="nakyeonko")

@app.route('/getTemperSeneorData')
def getTemperSeneorData():
    temper_sensor_value = read_csvfile.get_senor_data_last_value(file_name='temper_sensor.csv',name='temper')
    temper_sensor_value = float(temper_sensor_value)
    return jsonify({'sensor_data':temper_sensor_value})

@app.route('/getPHSensorData')
def getPHSensorData():
    sensor_value =read_csvfile.get_senor_data_last_value(file_name='sensor.csv',name='ph')
    sensor_value = float(sensor_value)
    return jsonify({'sensor_data':sensor_value})

@app.route('/turnOn')
def turnOn():
    mqtt_test.turnOn()
    return "1"

@app.route('/turnOff')
def turnOff():
    mqtt_test.turnOff()
    return "0"

@app.route('/servo_turnOn')
def servo_turnOn():
    servo_motor_control()
    return "2"

@app.route('/servo_motor_auto_mode')
def servo_motor_auto():
    auto_servo.start()
    return "4"

@app.route('/servo_motor_auto_mode_off')
def servo_motor_auto_off():
    auto_servo.stop()
    return "5"

if __name__ == '__main__':
    mqtt_test = Mqtt_class()
    mqtt_test.init()
    start_bmp_sensor_minutes()
    start_bmp_sensor()
    app.run(host='0.0.0.0', port=port, debug=True)