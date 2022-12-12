import paho.mqtt.client as mqtt
import time
# from make_csvfile import make_csvfile
from make_csvfile_class import Make_csvfile


# ph 센서 topic 명
topic = "ph_sensor_outTopic"

# 릴레이 topic 명
inTopic = "ph_relay_motor_inTopic"

# topic = "r_outTopic" 

class Mqtt_class:
  def __init__(self, IP='nakyeonkopi3.local', topic = "ph_outTopic", client_name="mainpy", file_name="sensor.csv"):
    self.IP = IP
    self.topic = topic
    self.client_name = client_name
    self.file_name = file_name
    self.makecsv_ph = Make_csvfile(file_name)

  def init(self):
    def on_connect(client, userdata, flags, rc):
      client.subscribe(topic)

    def on_message(client, userdata, msg):
      self.makecsv_ph.make_csvfile(sensor_value=msg.payload.decode("utf-8"))
    
    self.client = mqtt.Client(self.client_name)
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
