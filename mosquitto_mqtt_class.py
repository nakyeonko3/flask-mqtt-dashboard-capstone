import paho.mqtt.client as mqtt
import pandas as pd
import time
from datetime import datetime

# ph 센서
topic = "ph_outTopic"
inTopic = "test_inTopic"
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

class Mqtt_class:
  def __init__(self, IP='nakyeonkopi3.local', topic = "ph_outTopic"):
    self.IP = IP
    self.topic = topic

  def init(self):
    self.client = mqtt.Client()
    self.client.on_connect = on_connect
    self.client.on_message = on_message
    self.client.connect(self.IP) #접속할 호스트명
    self.client.loop_start()

  def turnOn(self):
    self.client.publish(inTopic, "1")

  def turnOff(self):
    self.client.publish(inTopic, "0")


count =0

if __name__ == "__main__":
    mqtt_test = Mqtt_class()
    mqtt_test.init()
    while count < 5:
      mqtt_test.turnOn()
      time.sleep(10)
      mqtt_test.turnOff()
      time.sleep(10)
      count = count +1
