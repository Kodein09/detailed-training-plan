import pandas as pd
import numpy as np

dataset = pd.read_csv("dirty_cafe_sales.csv", chunksize=10_000)

class ProcessingData:
    def drop_duplicates(self, df: pd.DataFrame):
        df = df.drop_duplicates()
        return df

    def data_typing(self, df: pd.DataFrame):
        #num
        for col in df.columns:
            if not pd.api.types.is_numeric_dtype(df[col]):
                num_conv = pd.to_numeric(arg=df[col], errors='coerce')
                if num_conv.notna().mean() > 0.7:
                    df[col] = num_conv
                    continue

            #date
            if df[col].dtype == 'object':
                date_conv = pd.to_datetime(arg=df[col], errors='coerce')
                if date_conv.notna().mean() > 0.7:
                    df[col] = date_conv
                    continue

            #str
            if df[col].dtype == 'object':
                num_unique = df[col].nunique()
                num_total = len(df)
                if num_unique / num_total < 0.5:
                    df[col] = df[col].astype('category')
        return df

    def missing_value(self, df: pd.DataFrame):
        num_col = df.select_dtypes(include=np.number).columns
        for col in num_col:
            df[col] = df[col].fillna(df[col].median())

        str_col = df.select_dtypes(include='object').columns
        for col in str_col:
            most_frequent = df[col].mode()
            if not most_frequent:
                df[col] = df[col].fillna(most_frequent[0])

        date_col = df.select_dtypes(include=np.datetime64).columns
        for col in date_col:
            df[col] = df[col].ffill().bfill()
        return df

    def optimize_memory(self, df: pd.DataFrame):
        for col in df.select_dtypes(include=np.number).columns:
            df[col] = pd.to_numeric(arg=df[col], downcast='integer' if 'int' in str(df[col].dtype) else 'float')
        return df

    def iqr(self, df: pd.DataFrame):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)

        IQR = Q3 - Q1

        for col in df.columns:
            condition = ((df[col] < (Q1[col] - 1.5 * IQR[col])|
                          df[col] > (Q3[col] + 1.5 * IQR[col])))

            df.loc[condition, col] = np.nan
        return df

    def z_score(self, df: pd.DataFrame):
        num_col = df.select_dtypes(include=np.number).columns
        df[num_col] = (df[num_col] - df[num_col].mean()) / df[num_col].std()
        return df

    def pipeline(self, df: pd.DataFrame):
        df = (df.pipe(self.drop_duplicates)
              .pipe(self.data_typing)
              .pipe(self.missing_value)
              .pipe(self.)
              )

process = ProcessingData()
print(process.)