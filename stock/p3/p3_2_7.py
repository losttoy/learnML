import pandas as pd

data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 'k2': [3, 2, 1, 3, 3, 4, 4]})
print(data)

d1 = data.drop_duplicates()
print(d1)
print(data[data.duplicated()])

d2 = data.drop_duplicates(subset=['k1'])
print(d2)
print(data[data.duplicated(subset=['k1'])])

d3 = data.drop_duplicates(subset=['k1'], keep='last')
print(d3)
