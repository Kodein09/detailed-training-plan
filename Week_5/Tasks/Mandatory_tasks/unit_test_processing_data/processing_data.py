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
        for col in df.select_dtypes(include='object').columns:
            num_unique = df[col].nunique()
            print(f"df[col]:\n{df[col]}")
            print(f"Unique numbers: {num_unique}")
            num_total = len(df)
            print(f"Total numbers: {num_total}")

            if num_unique / num_total <= 0.5:
                df[col] = df[col].astype('category')
        return df

    def iqr(self, df: pd.DataFrame):
        num_df = df.select_dtypes(include=np.number)
        Q1 = num_df.quantile(q=0.25)
        Q3 = num_df.quantile(q=0.75)

        IQR = Q3 - Q1

        for col in num_df.columns:
            print(f"Numbers df:\n{num_df}")
            print(f"Column: {col}")
            condition = ((df[col] < (Q1[col] - 1.5 * IQR[col])) |
                      (df[col] > (Q3[col] + 1.5 * IQR[col])))

            print(f"Condition: {condition}")
            print(f"df.loc[condition, col]: {df.loc[condition, col]}")
            df.loc[condition, col] = np.nan

        return df

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
        df = pd.DataFrame({
            "col1": [1,1,2,3],
            "col2": ["2025-12-01", "2025-12-01", "2025-12-04", "2025-12-04"],
            "col3": ["apple", "banana", "apple", "apple"]
        })

        result = self.test.category(df)

        self.assertNotEqual(result["col1"].dtype, "category")
        self.assertEqual(result["col2"].dtype, "category")
        self.assertEqual(result["col3"].dtype, "category")

    def test_iqr(self):
        df = pd.DataFrame({
            "col1": [1, 1, 2, 100],
            "col2": ["2025-12-01", "2025-12-01", "1909-12-04", "2025-12-04"],
            "col3": ["apple", "banana", "apple", "apple"]
        })

        result = self.test.iqr(df)

        expected = pd.DataFrame({
            "col1": [1, 1, 2, np.nan],
            "col2": ["2025-12-01", "2025-12-01", "1909-12-04", "2025-12-04"],
            "col3": ["apple", "banana", "apple", "apple"]
        })

        pd.testing.assert_frame_equal(result, expected)

    def test_zscore(self):
        df = pd.DataFrame({
            "col1": [1, 1, 2, 100],
            "col2": ["2025-12-01", "2025-12-01", "1909-12-04", "2025-12-04"],
            "col3": ["apple", "banana", "apple", "apple"]
        })

        result = self.test.z_score(df)
        print(result)

        expected = pd.DataFrame({
            "col1": [-0.50, -0.50, -0.48, 1.49],
            "col2": ["2025-12-01", "2025-12-01", "1909-12-04", "2025-12-04"],
            "col3": ["apple", "banana", "apple", "apple"]
        })

        pd.testing.assert_frame_equal(result, expected, atol=1e-2)