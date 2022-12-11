import Adafruit_BMP.BMP085 as BMP085
from make_csvfile_class import Make_csvfile
from dynamikontrol import Timer
import time

t2 = Timer()
temper_sensor_minutes = BMP085.BMP085(busnum=1)

bmpcsvminutes = Make_csvfile("temper_sensor_minute.csv")

def read_temperature_from_bmp_minutes():
    temper = temper_sensor_minutes.read_temperature()
    bmpcsvminutes.make_csvfile(sensor_value=temper)

def start_bmp_sensor_minutes():
    t2.callback_after(func =read_temperature_from_bmp_minutes, after=0,interval=60)

# def hello1():
#     print("test hello1")

if __name__ == "__main__":
    start_bmp_sensor_minutes()
    # t2.callback_after(func=hello1, after=1, interval=1)

# __name__이 정확하게 뭐지?
#왜 파이썬 스레드는 메인 코드 실행 전에 넣어야지 실행이될까?