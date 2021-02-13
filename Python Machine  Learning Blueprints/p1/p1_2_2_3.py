import inline as inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# %matplotlib inline
import numpy as np

fig, ax = plt.subplots(figsize=(6,4))
ax.hist(df['petal width'], color='black');
ax.set_ylabel('Count', fontsize=12)
ax.set_xlabel('Width', fontsize=12)
plt.title('Iris Petal Width', fontsize=14, y=1.01)