import paho.mqtt.client as mqtt
import time
import pandas as pd
from datetime import datetime

# ph 센서
topic = "ph_outTopic"
# 가변 저항
# topic = "r_outTopic" 


df = pd.DataFrame([], columns=['Date', 'Sensor'])

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)

def on_message(client, userdata, msg):
    make_csvfile(msg.payload.decode("utf-8"))

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
    client.connect('nakyeonkopi.local') #접속할 호스트명
    client.loop_start()


if __name__ == "__main__":
    mqtt_init()
    while True:
        time.sleep(1)
