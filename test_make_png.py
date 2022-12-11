import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('sensor.csv')
print(df)
print(df.head())

df['Sensor'] = df['Sensor'].astype(float)
# df.plot(x='Date', y='Sensor', figsize=(16, 8))
fig = df.plot(x='Date', y='Sensor', figsize=(16, 8)).get_figure()

fig.savefig('test.png')