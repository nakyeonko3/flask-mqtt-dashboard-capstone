from servo import servo_motor_control
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_mainpage():
    return "hello"

@app.route('/turnOn')
def turnOn():
    servo_motor_control()
    return "1"

@app.route('/turnOff')
def turnOff():
    # servo_motor_control()
    return "0"

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)