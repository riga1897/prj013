import pandas as pd

df = pd.read_excel('../data/winemag-data-130k.xlsx')

#Группировка
# country_df = df.groupby('country')
# print(country_df.price.mean())

# Сортировка
# df.sort_values(by='price', inplace=True, ascending=False)
# print(df.head().price)

# Агрегация
# new_df = df.groupby('country').agg({
#     'price': 'mean',
#     'points': 'mean'
# })
#
# print(new_df.head())


country_df = df.groupby('country')

first_rows = country_df.first()
print(first_rows)






