import pandas as pd
import numpy as np

data = pd.DataFrame(
    data={
        "A": [10,10,15],
        "B": [10, np.nan, 30],
        "C": [20, 40, np.nan]
    }
)

class DataQualityReport:
    def __init__(self):
        self.data_quality = {
            "dtypes": None,
            "missing_values": 0,
            "unique_values": 0,
            "duplicate_values": 0,
            "min": 0,
            "median": 0,
            "max": 0,
            "often_values": 0
        }

    #
    # def generate_report(self, df: pd.DataFrame):
    #     df_copy = df.copy()
    #     initial_rows = len(df)
    #     result = {}
    #
    #     #dupl values
    #     dupl = df_copy.drop_duplicates()
    #     self.data_quality["duplicate_values"] = initial_rows - len(dupl)
    #
    #     for col in df.columns:
    #         if np.issubdtype(df[col].dtype ,np.number):
    #             result[col] = {}
    #
    #             #dtype
    #             result[col]["dtypes"] = df_copy[col].dtypes
    #
    #             #unique values
    #             result[col]["unique_values"] = df_copy[col].nunique()
    #
    #             #often values
    #             result[col]["often_values"] = df_copy[col].mode().iloc[0]
    #
    #             #handle missing values
    #             result[col]["missing_values"] = df_copy[col].isnull().sum().sum()
    #             df_copy[col] = df_copy[col].fillna(value=df_copy[col].median())
    #
    #             #min, median, max
    #             result[col]["min"] = df_copy[col].min()
    #             result[col]["median"] = df_copy[col].median()
    #             result[col]["max"] = df_copy[col].max()
    #
    #
    #         elif df[col].dtype == 'object':
    #
    #             #unique values
    #             result[col]["unique_values"] = df_copy[col].nunique()
    #
    #             #often values
    #             result[col]["often_values"] = df_copy[col].mode().iloc[0]
    #
    #             #missing values
    #             result[col]["missing_values"] = df_copy[col].isnull().sum()
    #             df_copy[col] = df_copy.fillna(value=df_copy[col].median())
    #
    #         elif np.issubdtype(df[col].dtype, np.datetime64):
    #             #min, median, max
    #             result[col]["min"] = df_copy[col].min()
    #             result[col]["median"] = df_copy[col].median()
    #             result[col]["max"] = df_copy[col].max()
    #
    #     return result


    def generate_report(self, df: pd.DataFrame):
        result = {}

        for col in df.columns:
            result[col] = {}
            result[col]['dtypes'] = df[col].dtypes
            result[col]['missing_values'] = df[col].isnull().sum()
            result[col]['unique_values'] = df[col].nunique()
            result[col]['often_values'] = df[col].mode().iloc[0]

            if np.issubdtype(df[col].dtype, np.number):
                result[col]['min'] = df[col].min()
                result[col]['median'] = df[col].median()
                result[col]['max'] = df[col].max()

            elif np.issubdtype(df[col].dtype, np.datetime64):
                result[col]['min'] = df[col].min()
                result[col]['max'] = df[col].max()

        return result

dq = DataQualityReport()
print(dq.generate_report(data))