import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.set_printoptions(suppress=True)
np.set_printoptions(precision=4)


def normalize():
    aug = 100000
    data = pd.read_csv('raw.csv')

    for axis in ['latitude', 'longitude']:
        data[axis] *= aug
        lat_med = data[axis].median()
        data[axis] -= lat_med
        data[axis] = data[axis].apply(lambda x : round(x, 3))

    data.plot(x='longitude', y='latitude', kind='scatter')
    plt.savefig('graph.jpg')

    data.to_csv('normal.csv', index=False)


def matrix():
    data = pd.read_csv('normal.csv')

    side = len(data)
    loc = data['location'].unique()
    adj = np.zeros(shape=(side, side))

    langlen = len(data['latitude'])
    longlen = len(data['longitude'])

    for i in range(langlen):
        for j in range(longlen):
            
            p1 = data.loc[i]
            p2 = data.loc[j]
            
            dis = distance(p1['latitude'], p2['latitude'], p1['longitude'], p2['longitude'])
            adj[i][j] = dis

    adjdf = pd.DataFrame(adj, columns=loc, index=loc)
    adjdf.to_csv('adjacency.csv', index_label='compared') 


def distance(x1, x2, y1, y2):
    tmp1 = (x2 - x1) ** 2
    tmp2 = (y2 - y1) ** 2
    return math.sqrt(tmp1 + tmp2)


if __name__ == '__main__':
    normalize()
    matrix()
