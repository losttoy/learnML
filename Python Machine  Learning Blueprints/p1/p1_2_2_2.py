import os
import pandas as pd
import requests
PATH = r'/iris/'

# for speed
# r= requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
# with open(PATH + 'iris.data', 'w') as f:
#     f.write(r.text)

os.chdir(PATH)
df = pd.read_csv(PATH + 'iris.data', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
print(df.head())

print(df)

# print(df[:3, [x for x in df.columns if 'width' in x]])
print([x for x in df.columns if 'width' in x])
print(df[[x for x in df.columns if 'width' in x]])

print(df.count())

import matplotlib.pyplot as plt
plt.style.use('ggplot')
# %matplotlib inline
import numpy as np

# 直方图histogram（单个）
fig, ax = plt.subplots(figsize=(6,4))
ax.hist(df['petal width'], color='green');
ax.set_ylabel('Count', fontsize=12)
ax.set_xlabel('Width', fontsize=12)
plt.title('Iris Petal Width', fontsize=14, y=1.01)
plt.show()

# 直方图histogram（2*2）
fig, ax = plt.subplots(2,2, figsize=(6,4))
ax[0][0].hist(df['petal width'], color='black');
ax[0][0].set_ylabel('Count', fontsize=12)
ax[0][0].set_xlabel('Width', fontsize=12)
ax[0][0].set_title('Iris Petal Width', fontsize=14, y=1.01)
ax[0][1].hist(df['petal length'], color='black');
ax[0][1].set_ylabel('Count', fontsize=12)
ax[0][1].set_xlabel('Lenth', fontsize=12)
ax[0][1].set_title('Iris Petal Lenth', fontsize=14, y=1.01)
ax[1][0].hist(df['sepal width'], color='black');
ax[1][0].set_ylabel('Count', fontsize=12)
ax[1][0].set_xlabel('Width', fontsize=12)
ax[1][0].set_title('Iris Sepal Width', fontsize=14, y=1.01)
ax[1][1].hist(df['sepal length'], color='black');
ax[1][1].set_ylabel('Count', fontsize=12)
ax[1][1].set_xlabel('Length', fontsize=12)
ax[1][1].set_title('Iris Sepal Length', fontsize=14, y=1.01)
plt.tight_layout()
plt.show()

# scatter plot-散点图
# 高相关
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(df['petal width'],df['petal length'], color='green')
ax.set_xlabel('Petal Width')
ax.set_ylabel('Petal Length')
ax.set_title('Petal Scatterplot')
plt.show()

# scatter plot-散点图
# 低相关
fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(df['sepal width'],df['sepal length'], color='green')
ax.set_xlabel('sepal width')
ax.set_ylabel('sepal length')
ax.set_title('sepal Scatterplot')
plt.show()

# 线图
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(df['petal length'], color='blue')
ax.set_xlabel('Specimen Number')
ax.set_ylabel('Petal Length')
ax.set_title('Petal Length Plot')
plt.show()

# 线图
fig, ax = plt.subplots(figsize=(6,6))
bar_width = .8
labels = [x for x in df.columns if 'length' in x or 'width' in x]
ver_y = [df[df['class']=='Iris-versicolor'][x].mean() for x in labels]
vir_y = [df[df['class']=='Iris-virginica'][x].mean() for x in labels]
set_y = [df[df['class']=='Iris-setosa'][x].mean() for x in labels]
x = np.arange(len(labels))
ax.bar(x, vir_y, bar_width, bottom=set_y, color='darkgrey')
ax.bar(x, set_y, bar_width, bottom=ver_y, color='white')
ax.bar(x, ver_y, bar_width, color='black')
ax.set_xticks(x + (bar_width/2))
ax.set_xticklabels(labels, rotation=-70, fontsize=12);
ax.set_title('Mean Feature Measurement By Class', y=1.01)
ax.legend(['Virginica','Setosa','Versicolor'])
plt.show()
