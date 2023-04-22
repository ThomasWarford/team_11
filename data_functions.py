import pandas as pd

def one_hot_encode(df, column_name):
    one_hot = pd.get_dummies(df[column_name])
    df = df.drop(column_name, axis=1)
    df = df.join(one_hot)
    return df