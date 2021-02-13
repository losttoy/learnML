# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt
# %matplotlib inline
from matplotlib.font_manager import FontProperties

# def plot_para():#设置画图参数及相关配置,如透明度,中文啥啥的
#     mpl.rcParams['axes.unicode_minus']=False
#     #手动设置字体路径
#     return FontProperties(fname='/Users/zhuwei/PycharmProjects/learnML/stock/p3/msyh.ttf')
#
# #在设置绘图的部分指定FontProperties，比如
# plt.ylabel(u'T+4有效与T+1有效 GMV 比值',FontProperties=plot_para())

print(matplotlib.matplotlib_fname())

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
mpl.rcParams['font.size'] = 12  # 字体大小
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# font = {
#     'family':'SimHei',
#     'weight':'bold',
#     'size':12
# }
# matplotlib.rc("font", **font)
# plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号

data = pd.read_csv('data.csv', index_col='Date')
print(data.head())
data.index = [dt.datetime.strptime(x, '%Y-%m-%d') for x in data.index]
print(data.head())

data.plot(figsize=(10, 6))
plt.ylabel('涨跌幅')
plt.show()

import statsmodels.api as sm
x = data['沪深300'].values
X = sm.add_constant(x)
y = data['中国平安'].values

model = sm.OLS(y, X)
results = model.fit()
print(results.params)
print(results.fittedvalues)

# 拟合
# 相关性强
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='平安-沪深')
plt.plot(x, results.fittedvalues, 'r--', label='线性回归')
plt.legend() # 添加附注
plt.show()

import numpy.random as npr
factor = npr.rand(1000, 3)
print(factor)
FACTOR = sm.add_constant(factor)

fac1 = factor[:, 0]  #因子1
fac2 = factor[:, 1]  #因子2
fac3 = factor[:, 2]  #因子3
e = npr.random(1000)  #噪声
port = fac1 * 0.3 + fac2 * 0.7 + fac3 * 0.4 + e  #虚构投资组合及因子权重
port = fac1 * 0.3 + fac2 * 0.7 + fac3 * 0.4  #虚构投资组合及因子权重
model1 = sm.OLS(port, FACTOR)
results1 = model1.fit()
print(results1.params)