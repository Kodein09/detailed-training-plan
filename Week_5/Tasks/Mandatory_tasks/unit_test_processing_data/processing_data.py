import pandas as pd
import numpy as np

dataset = pd.read_csv("dirty_cafe_sales.csv")

class ProcessingData:
    def drop_dupl(self, df: pd.DataFrame):
        df = df.drop_duplicates()
        return df

    def data_types(self, df: pd.DataFrame):
        #num
        for col in df.columns:
            num_conv = pd.to_numeric(arg=df[col], errors='coerce')
            if num_conv.notna().all():
                df[col] = num_conv.astype(int)
            elif num_conv.notna().any():
                df[col] = num_conv.astype("Int64")

        #date
        for col in df.columns:
            if df[col].dtype == 'object':
                date_conv = pd.to_datetime(arg=df[col], errors='coerce')
                if date_conv.notna().mean() > 0.7:
                    df[col] = date_conv

        return df

    def missing_value(self, df: pd.DataFrame):

        num_col = df.select_dtypes(include=np.number).columns
        df[num_col] = df[num_col].fillna(value=df[num_col].median())

        date_col = df.select_dtypes(include=np.datetime64).columns
        df[date_col] = df[date_col].ffill().bfill()

        str_col = df.select_dtypes(include='object').columns
        df[str_col] = df[str_col].fillna(value='Unknown')

        df = df.replace(to_replace=["UNKNOWN", "ERROR", "Unknown"], value=np.nan)

        for col in str_col:
            most_frequent = df[col].mode()
            if not most_frequent.empty:
                df[col] = df[col].fillna(value=most_frequent.iloc[0])

        return df

    def category(self, df: pd.DataFrame):
        str_col = df.select_dtypes(include='object').columns
        df[str_col] = df[str_col].astype(dtype='category')
        return df

    def iqr(self, df: pd.DataFrame):
        num_df = df.select_dtypes(include=np.number)
        Q1 = num_df.quantile(q=0.25)
        Q3 = num_df.quantile(q=0.75)

        IQR = Q3 - Q1

        condition = ~((num_df < (Q1 - 1.5 * IQR)) |
                      (num_df > (Q3 + 1.5 * IQR))).any(axis=1)

        return df[condition]

    def z_score(self, df: pd.DataFrame):
        num_col = df.select_dtypes(include=np.number).columns
        df[num_col] = (df[num_col] - df[num_col].mean()) / df[num_col].std()
        return df

    def pipeline(self, df: pd.DataFrame):
        df = (
            df.pipe(self.drop_dupl)
            .pipe(self.data_types)
            .pipe(self.missing_value)
            .pipe(self.iqr)
            .pipe(self.z_score)
            .pipe(self.category)
        )
        return df

# process = ProcessingData()
# print(process.pipeline(dataset))

import unittest
class TestProcessingData(unittest.TestCase):
    def setUp(self):
        self.test = ProcessingData()

    def test_drop_duplicates(self):
        df = pd.DataFrame([1,2,2,3])
        result = self.test.drop_dupl(df)
        self.assertEqual(len(result), 3)

    def test_data_types(self):
        df = pd.DataFrame({
            "col1": ["1", "2", "3", np.nan],
            "col2": ["2025-12-01", "2025-12-02", "not a date", "2025-12-04"],
            "col3": ["apple", "banana", None, "apple"]
        })

        result = self.test.data_types(df)

        expected = pd.DataFrame({
            "col1": pd.Series([1, 2, 3, np.nan], dtype="Int64"),
            "col2": pd.to_datetime(["2025-12-01", "2025-12-02", "not a date", "2025-12-04"], errors='coerce'),
            "col3": ["apple", "banana", None, "apple"]
        })

        # print(f"Data types from dataframe:\n{df.dtypes}\n")
        # print(f"Data types from expected:\n{expected.dtypes}\n")

        pd.testing.assert_frame_equal(result, expected)

    def test_missing_value(self):
        df = pd.DataFrame({
            "datetime": ["2026-01-01", np.nan, "2026-01-03"],
            "number": ["1", np.nan, "4"],
            "string": ["Apple", "Banan", np.nan]
        })

        result = self.test.missing_value(df)

        expected = pd.DataFrame({
            "datetime": ["2026-01-01", "2026-01-01", "2026-01-03"],
            "number": ["1", "1", "4"],
            "string": ["Apple", "Banan", "Apple"]
        })

        pd.testing.assert_frame_equal(result, expected, check_dtype=True)

    def test_category(self):
        pass

    def test_iqr(self):
        result = self.test.iqr()

        pass

    def test_zscore(self):
        pass