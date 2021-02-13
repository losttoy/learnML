# ordinary least squares
import pandas as pd
data = pd.read_csv('data.csv', index_col='Date')

print(data)

hs300 = data.iloc[:, [0]]
pingan = data.iloc[:, [1]]

# x
print(hs300)
print(hs300.describe())
x_mean = hs300.mean().values
# y
print(pingan)
print(pingan.describe())
y_mean = pingan.mean().values

# print(hs300.values)
# print(pingan.values)
multi = hs300.values * pingan.values
print(multi)

multiDataFrame = pd.DataFrame(multi)
print(multiDataFrame.describe())

xy_mean = multiDataFrame.mean().values
xx_mean = pd.DataFrame(hs300.values * hs300.values).mean().values

k = (xy_mean - x_mean * y_mean) / (xx_mean - x_mean * x_mean)
print("k=%s,x=%s,y=%s"%(k, x_mean, y_mean))
# y = k * x + b -> b = y - k * x
b = y_mean - k * x_mean
print("y = %s * x + %s"%(k, b))