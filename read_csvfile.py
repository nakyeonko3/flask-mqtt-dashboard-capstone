import pandas as pd
import re
import time

error_data = {
    "ph":0,
    "ph2":0,
    "temper":0
}


def get_senor_data_last_value(file_name, name):
    try:
        df = pd.read_csv(file_name)
        last_number = df['Sensor'].values[-1]
        error_data[name] = last_number
        return last_number
    except:
        return error_data[name]
    #csv file 마지막 줄의 Sensor 값을 가져옴

def get_senor_data_last_value_memory(file_name):
    df = pd.read_csv(file_name, delimiter=',')
    list_of_rows = [{'date':row[0], 'sensor':row[1] }for row in df.values]
    return list_of_rows





if __name__ == "__main__":
    #print(read_csv_Date_value_last())
    # print(read_csv_Sensor_value_last())
    # print(int(get_senor_data_last_value(file_name='csvtemper_sensor.csv')))
    sensor_data = get_senor_data_last_value_memory(file_name='csv/temper_sensor.csv')
    print(sensor_data)

    # string = 'aaa1234, ^&*2233pp'
    # numbers = re.sub(r'[^0-9]', '', string)
    # print(numbers)


