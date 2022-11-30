import paho.mqtt.client as mqtt
import time
import pandas as pd
from datetime import datetime
import random

topic = "outTopic"

sensordata = ""

df = pd.DataFrame([], columns=['Date', 'Sensor'])

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)

def on_message(client, userdata, msg):
    global sensordata
    sensordata = msg.payload.decode("utf-8")
    make_csvfile(sensordata)

def make_csvfile(sensor_value):
    global df
    new_line = pd.DataFrame({
            'Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
            'Sensor': [sensor_value]
            })
    df = pd.concat([df, new_line], ignore_index=True)
    df.to_csv('sensor.csv', index=False)

def mqtt_init():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('localhost')
    client.loop_start()


if __name__ == "__main__":
    mqtt_init()
    count = 0
    while True:
        time.sleep(1)
        count = count +1
