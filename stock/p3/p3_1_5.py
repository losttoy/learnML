import numpy.random as npr
import matplotlib.pyplot as plt

size = 1000
print("1、")
print(npr.rand(size, 3))
print("2、")
print(npr.randn(size))
print("3、")
print(npr.randint(0, 10, size))
print("4、")
print(npr.choice([0, 10, 20, 30, 40], size))

fig, ax = plt.subplots(2,2,figsize=(10,10))
# 0-1之间的三列随机数
ax[0][0].hist(npr.rand(size, 3))
# 正太分布
ax[0][1].hist(npr.randn(size))
# 0-10之间的随机整数
ax[1][0].hist(npr.randint(0, 10, size))
# 给定数组的随机样本
ax[1][1].hist(npr.choice([0, 10, 20, 30, 40], size))
plt.show()

fig, ax = plt.subplots(2,2,figsize=(10,10))
# n=100，p=0.3的二项分布
ax[0][0].hist(npr.binomial(100,0.3,size))
# 均值为10，标准差=2的正态分布
ax[0][1].hist(npr.normal(10, 20, size))
# 自由度为0.5的卡方分布
ax[1][0].hist(npr.chisquare(0.5, size))
# x为2的泊松分布
ax[1][1].hist(npr.poisson(2.0, size))
plt.show()