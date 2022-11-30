# https://stackoverflow.com/questions/64592277/flask-mqtt-on-connect-is-never-called-when-used-with-socketio
# Flask socketIO server with classical Paho MQTT  
# Unlike the Flask-MQTT version, this correctly calls MQTT on_connect()

from flask import Flask, render_template
import paho.mqtt.client as mqtt
from flask_socketio import SocketIO

sub_topic = 'my/sub/topic'
pub_topic = 'my/pub/topic'
server = 'localhost'
MQTTport = 1883
client = None

app = Flask(__name__)
socketio = SocketIO (app, async_mode='gevent', cors_allowed_origins="*") 

# SocketIO

@socketio.on('connect')
def on_connect ():
    print ('Socket client connected.')
    socketio.send ('Socket server ready.')

@socketio.on ('message')    
def on_publish (payload):
    client.publish (pub_topic, payload)
    
# MQTT
   
def on_connect (client, userdata, flags, rc):
    print('* Connected to MQTT broker *')
    client.subscribe (sub_topic, qos=0)  
    client.publish (pub_topic, 'MQTT server ready.')

def on_message (client, userdata, msg):
    socketio.send (msg.payload.decode())

# HTTP

@app.route('/')
def index():
    return render_template('bridge.html')
    
# Main  
  
client = mqtt.Client("Mqtt-socket-bridge-2021", clean_session=True)   
client.on_connect = on_connect
client.on_message = on_message
client.connect(server, MQTTport, keepalive=60)

print ('Starting the MQ loop..')
client.loop_start()   

print ('Starting the socket server on port 5000...')    
socketio.run (app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)