import pandas as pd
import numpy as np

data = pd.DataFrame(
    data={
        "Employee": ["Dave", "Pit", "Bob"],
        "Salary": [100, 200, 150],
        "Working_hours": [8, 7, 8]
    }
)

# def detect_types_int(df: pd.DataFrame):
#     df_copy = df.copy()
#
#     to_numeric = df_copy.select_dtypes(include=np.number)
#     for col in df_copy.iterrows():
#         df_copy[col] = df_copy[to_numeric]
#
#     return df_copy.dtypes
#
# def detect_types_datetime(df: pd.DataFrame):
#     df_copy = df.copy()
#
#     for column in df_copy.columns:
#         df[column] = pd.to_datetime(df_copy[column])
#         continue
#
#     return df_copy.dtypes


# def detect_types_int(df: pd.DataFrame):
#     df_copy = df.copy()
#
#     for col in df_copy.columns:
#         try:
#             df_copy[col] = pd.to_numeric(df_copy[col])
#             continue
#         except:
#             pass
#
#     return df_copy.dtypes
#
# def detect_types_datetime(df: pd.DataFrame):
#     df_copy = df.copy()
#
#     for col in df_copy.columns:
#         try:
#             df_copy[col] = pd.to_datetime(df_copy[col])
#             continue
#         except:
#             pass
#
#     return df_copy.dtypes
#
# print(detect_types_int(data))
# print(detect_types_datetime(data))


def detect_types(df: pd.DataFrame):
    df_copy = df.copy()
    for col in df_copy.columns:
        try:
            df_copy[col] = pd.to_numeric(df_copy[col], errors='ignore')
            df_copy[col] = pd.to_datetime(df_copy[col])
        except Exception as e:
            f"Exceptions: {str(e)}"
    return df_copy.dtypes

print(detect_types(data))