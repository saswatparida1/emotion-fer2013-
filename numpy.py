
import pandas as pd
import numpy as np


data = pd.read_csv('./fer2013.csv')
data1 = data['pixels']
data1 = [ dat.split() for dat in data1]
data1 = np.array(data1)
data1 = data1.astype('float64')
data1 = [[np.divide(d,255.0) for d in dat] for dat in data1]


data2 = data['emotion']


np.save('./data/Scaled.bin.npy',data1)
np.save('./data/Labeel.bin.npy',data2)
