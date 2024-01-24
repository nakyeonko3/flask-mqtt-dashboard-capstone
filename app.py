# https://stackoverflow.com/questions/43205568/python-flask-server-with-mqtt-subscription

from flask import Flask, render_template, jsonify

import read_csvfile

port = 5000

app = Flask(__name__)
port = 5000
TEMPER_SENSOR_CSV = "csv/temper_sensor.csv"
sensor_data = read_csvfile.get_senor_data_last_value_memory(TEMPER_SENSOR_CSV)


@app.get("/getTemperSeneorData")
def getTemperSeneorData_Memory():
    temper_sensor_value = float(sensor_data[12]["sensor"])
    return jsonify({"sensor_data": temper_sensor_value})


@app.route("/")
def render_mainpage():
    return render_template("index.html", name="nakyeonko")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
