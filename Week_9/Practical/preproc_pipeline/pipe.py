import numpy as np
import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, RobustScaler


pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

dataset = pd.read_csv("../train.csv")

class PreprocessingData:
    def missing_value(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Заполняет пропуски медианой в числовых столбцах.
        :param df: pd.DataFrame
        :return: pd.DataFrame
        """
        df = df.copy()
        scaler = RobustScaler()
        for col in df.columns:
            if np.issubdtype(df[col], np.number):
                if col in ['Survived', 'PassengerId']:
                    continue
                df[col] = df[col].fillna(df[col].median())
                df[col] = scaler.fit_transform(df[[col]])[:, 0]
        return df

    def label_encoder(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Преобразует все уникальные категориальные признаки в числовую последовательность (от 0 до N - 1).
        :param df: pd.DataFrame
        :return: pd.DataFrame
        """
        df = df.copy()
        le = LabelEncoder()
        for col in df.columns:
            if df[col].nunique() > 3 and df[col].dtype in ['object', 'category']:
                df[col] = df[col].fillna('Unknown')
                df[col] = le.fit_transform(df[col].astype(str))
        return df

    def one_hot_encoder(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Преобразует уникальные значения категориального признака и создаёт для них новые столбцы в бинарном формате
        (0 и 1).
        :param df: pd.DataFrame
        :return: pd.DataFrame
        """
        df = df.copy()
        ohe = OneHotEncoder(sparse_output=False, dtype=int, handle_unknown='ignore')
        for col in df.columns:
            if df[col].nunique() <= 3 and df[col].dtype in ['object', 'category']:
                df[col] = df[col].fillna(df[col].mode()[0])
                encoded_arr = ohe.fit_transform(df[[col]])
                col_names = ohe.get_feature_names_out([col])
                encoded_df = pd.DataFrame(
                    data=encoded_arr,
                    columns=col_names,
                    index=df.index
                )
                df = pd.concat([encoded_df, df], axis=1)
                df = df.drop(columns=[col])
        return df

    def dummies(self, df: pd.DataFrame) -> pd.DataFrame:
        """Делает то же самое, что и OneHotEncoder."""
        df = df.copy()
        for col in df.columns:
            if df[col].dtype in ['object', 'category'] and df[col].nunique() <= 3:
                df[col] = df[col].fillna(df[col].mode()[0])
                dummies = pd.get_dummies(df[col])
                pd.concat([df, dummies], axis=1)

        return df

    def pipe(self, df: pd.DataFrame) -> pd.DataFrame:
        df = (df.pipe(self.label_encoder)
        .pipe(self.missing_value)
        .pipe(self.one_hot_encoder))
        return df

prep = PreprocessingData()
print(prep.pipe(dataset.head(100)))