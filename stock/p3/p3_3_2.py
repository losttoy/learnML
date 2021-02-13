import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv('data1.csv')
data1.head()

import scipy.interpolate as spi

X = data1.index  #定义数据点
Y = data1.values  #定义数据点
x = np.arange(0, len(data1), 0.15)  #定义观测点

ipo1 = spi.splrep(X,Y,k=1) #k 样条拟合顺序（1<=k<=5）
ipo3 = spi.splrep(X,Y,k=3)

iy1 = spi.splev(x,ipo1)
iy3 = spi.splev(x,ipo3)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,12))
ax1.plot(X, Y, label='沪深300')
ax1.plot(x, iy1, 'r.', label='插值点')
ax1.set_ylim(Y.min() - 10, Y.max() + 10)
ax1.set_ylabel('指数')
ax1.set_title('线性插值')
ax1.legend()
ax2.plot(X, Y, label='沪深300')
ax2.plot(x, iy3, 'r.', label='插值点')
ax2.set_ylim(Y.min() - 10, Y.max() + 10)
ax2.set_ylabel('指数')
ax2.set_title('三次样条插值')
ax2.legend()
plt.show()