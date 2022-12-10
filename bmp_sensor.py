import Adafruit_BMP.BMP085 as BMP085
from make_csvfile_class import Make_csvfile
from dynamikontrol import Timer
import time

t1 = Timer()
temper_sensor = BMP085.BMP085(busnum=1)

bmpcsv = Make_csvfile("temper_sensor.csv")

def read_temperature_from_bmp():
    temper = temper_sensor.read_temperature()
    bmpcsv.make_csvfile(sensor_value=temper)

def start_bmp_sensor():
    t1.callback_after(func =read_temperature_from_bmp, after=0,interval=1)

# def hello1():
#     print("hello")

if __name__ == "__main__":
    start_bmp_sensor()
    # t1.callback_after(func=hello1, after=1, interval=1)

#왜 파이썬 스레드는 메인 코드 실행 전에 넣어야지 실행이될까?