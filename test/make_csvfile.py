import pandas as pd
import time
from datetime import datetime

df = pd.DataFrame([], columns=['Date', 'Sensor'])

def make_csvfile(sensor_value, file_name = 'sensor.csv'):
    global df
    new_line = pd.DataFrame({
            'Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
            'Sensor': [sensor_value]
            })
    df = pd.concat([df, new_line], ignore_index=True)
    df.to_csv(file_name, index=False)
