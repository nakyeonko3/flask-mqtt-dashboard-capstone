from read_csvfile import get_senor_data_last_value
from time import sleep
from mosquitto_mqtt_class import Mqtt_class
from threading import Event, Thread
from servo import Auto_Thread

ph_value = 0.0
autopump = Mqtt_class(client_name="autopump")
autopump.init()

def read_ph_csv(event):
    while True:
        ph_value = get_senor_data_last_value(name="ph",file_name="sensor.csv")
        ph_value = float(ph_value)
        if ph_value > 8.5 or ph_value <7.5:
            autopump.turnOn()
            sleep(3)
            autopump.turnOff()
        sleep(1)
        if event.is_set():
            break

if __name__ == "__main__":
   auto_pump_thread = Auto_Thread(func=read_ph_csv)
   auto_pump_thread.start()
   sleep(10)
   auto_pump_thread.stop()


#1분에 한 번씩 읽고 



# 7.5 미만 8.5초과시 펌프 작동


#auto pump start

#auto pump stop
