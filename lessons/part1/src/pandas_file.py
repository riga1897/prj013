import pandas as pd

# df = pd.DataFrame({'Yes': [130, 50, 25], 'No': [50, 56, 100]})
# print(df)

df = pd.read_excel('../data/excel.xlsx')

print(df.shape)
print(df.head())