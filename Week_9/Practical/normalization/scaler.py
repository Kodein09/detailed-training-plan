# В машинном обучении есть признаки с совершенно разными масштабами, например, цена билета от 0 до 512, в таком случае
# модель может решить, что цена билета важнее, потому что числа там больше. Чтобы этого не происходило данные
# масштабируют и для этого имеется 3 базовых трансформера: MinMaxScaler, StandardScaler, RobustScaler.
# Все 3 трансформера делают одну работу (масштабирование числовых признаков), но математически подходят к ней по-разному.


import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler


pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# ---MinMaxScaler---
# (Нормализация) Сжимает число в строгий диапазон от 0 до 1 (диапазон можно настроить), формула:
# X(new) = (X - X(min))/X(max) - X(min)
def min_max_scaler(df: pd.DataFrame, columns_to_scale: list) -> pd.DataFrame:
    df = df.copy()
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())

    for col in columns_to_scale:
        if col in columns_to_scale and np.issubdtype(df[col], np.number):
            df[col] = MinMaxScaler().fit_transform(df[[col]])[:, 0]
    return df

# ---StandardScaler---
# (Стандартизация) Сдвигает данные так, чтобы их среднее значение (mu) стало равно 0, а стандартное отклонение
# (sgn/signum/std) стало равно 1, формула:
# X(new) = (X - mu)/sgn
def standard_scaler(df: pd.DataFrame, columns_to_scale: list) -> pd.DataFrame:
    df = df.copy()
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())

    for col in columns_to_scale:
        if col in columns_to_scale and np.issubdtype(df[col], np.number):
            df[col] = StandardScaler().fit_transform(df[[col]])[:, 0]
    return df

# ---RobustdScaler---
# (Масштабирование устойчиво к выбросам, аномалиям)
# Очень хорошо справляется с большими выбросами, аномалиями. Вместо среднего значения и минимумов используется
# медиана и квартили (IQR - межквартальный размах), формула:
# X(new) = (X - Median)/75 quartile - 25 quartile
def robust_scaler(df: pd.DataFrame, columns_to_scale: list) -> pd.DataFrame:
    df = df.copy()
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())

    for col in columns_to_scale:
        if col in columns_to_scale and np.issubdtype(df[col], np.number):
            df[col] = RobustScaler().fit_transform(df[[col]])[:, 0]
    return df

dataset = pd.read_csv("../train.csv")
# print(min_max_scaler(dataset.head(10), ['Age', 'Fare']))
# print(standard_scaler(dataset.head(10), ['Age', 'Fare']))
# print(robust_scaler(dataset.head(10), ['Age', 'Fare']))