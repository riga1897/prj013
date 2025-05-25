import pandas as pd

# Чтение CSV файла в DataFrame
df = pd.read_csv('titanic.csv')


def filter_and_sort_passengers(dataframe):
    # Фильтрация по условиям
    filtered_df = dataframe[(dataframe['fare'] > 50) & (dataframe['age'] < 30)]

    # Сортировка по имени
    sorted_df = filtered_df.sort_values(by='name')

    return sorted_df


# Пример использования функции
result = filter_and_sort_passengers(df)
print(result)