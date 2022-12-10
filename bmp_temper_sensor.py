import Adafruit_BMP.BMP085 as BMP085
import time
from make_csvfile import make_csvfile

temper_sensor = BMP085.BMP085(busnum=1)

while True:
    time.sleep(1)
    temper = temper_sensor.read_temperature()
    make_csvfile(file_name="temper_sensor.csv", sensor_value=temper)