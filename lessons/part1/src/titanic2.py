import pandas as pd
import json

def filter_passengers(df):
    result_df = df[((df['Sex'] == 'male') & (df['Age'] > 50)) | ((df['Sex'] == 'female') & (df['Age'] < 30))]
    return result_df.to_json(orient='records')