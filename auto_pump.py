from read_csvfile import get_senor_data_last_value
from time import sleep
from mosquitto_mqtt_class import Mqtt_class
ph_value = 0.0

autopump = Mqtt_class(client_name="autopump")
autopump.init()

def read_ph_csv():
    while True:
        ph_value = get_senor_data_last_value(name="ph",file_name="sensor.csv")
        ph_value = float(ph_value)
        if ph_value > 8.5 or ph_value <7.5:
            print("warning")
        sleep(10)



#1분에 한 번씩 읽고 



# 7.5 미만 8.5초과시 펌프 작동


#auto pump start

#auto pump stop
