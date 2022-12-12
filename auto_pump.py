from read_csvfile import get_senor_data_last_value
from time import sleep
from mosquitto_mqtt_class import Mqtt_class
from threading import Event, Thread
from servo import Auto_Thread



def check_ph(ph_value):
    if ph_value > 8.5 or ph_value <7.5:
        return False
    else:
        return True

def read_ph_csv():
    ph_value = get_senor_data_last_value(name="ph2",file_name="ph_sensor_minutes.csv")
    return float(ph_value)

def auto_pump_start(event, interval=1):
    autopump = Mqtt_class(file_name="ph_sensor_minutes.csv", client_name="autopump")
    autopump.init()
    while True:
        if check_ph(read_ph_csv()):
            autopump.turnOn()
            sleep(3)
            autopump.turnOff()
        if event.is_set():
            break
        sleep(interval)

 

if __name__ == "__main__":
   auto_pump_thread = Auto_Thread(func=auto_pump_start)
   auto_pump_thread.start()
   sleep(10)
   auto_pump_thread.stop()


#1분에 한 번씩 읽고 



# 7.5 미만 8.5초과시 펌프 작동


#auto pump start

#auto pump stop
