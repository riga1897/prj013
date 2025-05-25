import pandas as pd

# df = pd.read_excel('../data/winemag-data-130k.xlsx')

#df.set_index('title', drop=False, inplace=True)

# print(df.iloc[0])
# print(df.loc['Nicosia 2013 VulkГ  Bianco  (Etna)'])

# italy_wine = df.loc[df.country == 'Italy']
# print(italy_wine.head())

# df['description_length'] = df.description.map(len)
# #print(df)
# print(df.description_length.describe())

# Создадим DataFrame
# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })

# result = df.apply(pd.Series.mean)
# print(result)
#
# def range_of_series(series):
#     return series.max() - series.min()

# Используем apply для применения функции
# result = df.apply(range_of_series)
# print(result)

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
# })

# result = df.sum(axis=0)
# print(result)
#
# result = df.sum(axis=1)
# print(result)

df = pd.read_excel('../data/winemag-data-130k.xlsx')

def calc_avg(points):
    return sum(points) / len(points)

print(df['points'].apply(lambda x: calc_avg([x])))