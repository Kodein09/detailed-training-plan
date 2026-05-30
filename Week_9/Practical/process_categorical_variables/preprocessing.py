import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# Нормализация, кодирует метки значениями от 0, n_classes - 1. Этот трансформатор следует использовать только на
# целевые данные у, но никак не на входные данные Х.
# Основная задача LabelEncoder - кодировать целевую переменную (y), если она текстовая.


#LabelEncoder
# le = LabelEncoder()
# x = [10, 20, 30, 40, 40, 40, 50, 50]
# print(f"LabelEncoder.fit(x): {le.fit(x)}")
# print(f"LabelEncoder.classes_: {le.classes_}")
# print(f"LabelEncoder.transform(x): {le.transform(x)}")
# print(f"LabelEncoder.inverse_transform([0 1 2 3 3 3 4 4]): {list(le.inverse_transform([0, 1, 2, 3, 3, 3, 4, 4]))}")

# target_y = pd.Series(['positive', 'negative', 'neutral', 'positive', 'negative'])
# print(f"сырые данные у: {target_y.values}")
#
# le = LabelEncoder()
# encoded_y = le.fit_transform(target_y)
# print(f"Закодированные данные у: {encoded_y}, Это то, что пойдёт в модель")
#
# print(le.classes_)
# for number, text in enumerate(le.classes_):
#     print(f"Цифра: {number}, Текст: {text}")
#
# model_prediction = [2, 0]
# original_labels = le.inverse_transform(model_prediction)
# print(original_labels)

# train = ['Чипсы', 'Мороженое', 'Чипсы и Мороженое']
# le = LabelEncoder()
# print(f"Raw data: {train}")
#
# encoded = le.fit_transform(train)
# print(f"Encoded data: {train} -> {encoded}")
# print(f"This is what was learned via 'fit': {le.classes_} also was sorted in alphabetical order.")
#
# decoded = le.inverse_transform(encoded)
# print('Decode:', decoded)
# model_prediction = [2,2,0,1,0,0,0,1,1,1,1,1,2,2,2,2,2,2]
# print(f"Decode: {list(le.inverse_transform(model_prediction))}")

#OneHotEncoder
# dataset = pd.read_csv("../train.csv")
#
# object_df = dataset.head().select_dtypes('object')
# # print(object_df.info())
#
# ohe = OneHotEncoder(sparse_output=False, handle_unknown='error')
# encode = ohe.fit_transform(object_df)
# print(f"Encoded in sparse matrix (sparse_output=False):\n{encode}\n")
#
# decode = ohe.inverse_transform(encode)
# print(f"Decoded:\n{decode}")


#get_dummies
# dataset = pd.read_csv("../train.csv")
# categorical_data = dataset[['Embarked', 'Sex']].head(10)
# get_dummies = pd.get_dummies(categorical_data, drop_first=True, prefix_sep='_dummies_', dtype=int)
# print(get_dummies)

class DataPreprocessing:
    def to_label_encoder(self, df: pd.DataFrame) -> pd.DataFrame:
        le = LabelEncoder()
        df = df.copy()
        for col in df.columns:
            if df[col].nunique() <= 3:
                df[col] = le.fit_transform(df[col])
        return df

    def to_one_hot_encoder(self, df: pd.DataFrame) -> pd.DataFrame:
        """Преобразует категориальные данные в бинарные (0, 1)"""
        one_hot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        for col in df.columns:
            if df[col].nunique() <= 3:
                df = pd.concat([df, pd.DataFrame(one_hot_encoder.fit_transform(df[[col]]).toarray())], axis=1)
        return df

    def to_dummies(self, df: pd.DataFrame) -> pd.DataFrame:
        """Преобразует категориальные данные в бинарные (0, 1)"""
        df = df.copy()
        for col in df.columns:
            if df[col].nunique() <= 3:
                dummies = pd.get_dummies(df[col], prefix=col, prefix_sep='_dum_', dtype=int, dummy_na=True)
                df = pd.concat([df, dummies], axis=1)
                df = df.drop(columns=[col])
        return df


data = pd.read_csv("../train.csv")
one_hot_encoding = OneHotEncoding()
print(one_hot_encoding.to_label_encoder(data.head(10)))
# print(one_hot_encoding.to_one_hot_encoder(data.head(10)))
# print(one_hot_encoding.to_dummies(data.head(10)))
