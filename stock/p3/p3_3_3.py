import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import statsmodels.api as sm

data2 = pd.read_csv('data2.csv', index_col='Date')
data2.index = [dt.datetime.strptime(x, '%Y-%m-%d').strftime("%Y-%m-%d") for x in data2.index]
print(data2.head())

print("起始日期证券价格归一")
(data2 / data2.iloc[0]*100).plot(figsize=(10,6))
plt.xlabel('股价')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

print("百分比指数化")
print(data2.pct_change())
log_returns = np.log(data2.pct_change() + 1)
print(log_returns.head())

log_returns.hist(bins=50, figsize=(10,6), layout=(2, 3))

fig, axes = plt.subplots(3, 2, figsize=(10, 12))
for i in range(0, 3):
    for j in range(0, 2):
        sm.qqplot(log_returns.iloc[:, 2 * i + j].dropna(), line='s', ax=axes[i, j])
        axes[i, j].grid(True)
        axes[i, j].set_title(log_returns.columns[2 * i + j])
        axes[i, j].set_xlabel('理论分位数')
        axes[i, j].set_ylabel('样本分位数')
plt.subplots_adjust(wspace=0.3, hspace=0.4)
plt.show()