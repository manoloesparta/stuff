import pandas as pd
import matplotlib.pyplot as plt

aug = 100000
data = pd.read_csv('raw.csv')

data['latitude'] *= aug
lat_med = data['latitude'].median()
data['latitude'] -= lat_med

data['longitude'] *= aug
long_med = data['longitude'].median()
data['longitude'] -= long_med

data.plot(x='latitude',y='longitude',kind='scatter')
plt.savefig('graph.jpg')

data.to_csv('normal.csv')