import pandas as pd
import time
from datetime import datetime

class Make_csvfile():
    def __init__(self, file_name="sensor.csv"):
        self.df = pd.DataFrame([], columns=['Date', 'Sensor'])
        self.file_name = file_name

    def make_csvfile(self, sensor_value, file_name = "sensor.csv"):
        new_line = pd.DataFrame({
                'Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                'Sensor': [sensor_value]
                })
        self.df = pd.concat([self.df, new_line], ignore_index=True)
        self.df.to_csv(self.file_name, index=False)




# 처음에 설정한 파일 이름을 설정해주고, df도 설정해주고
# 메서드로 csv 파일을 만들어주면 됨.
