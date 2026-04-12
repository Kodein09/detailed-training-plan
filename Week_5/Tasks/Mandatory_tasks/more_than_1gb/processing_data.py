import pandas as pd
import numpy as np

dataset = pd.read_csv("dirty_cafe_sales.csv")
csv_total_weight = dataset.memory_usage(deep=True).sum() / (1024**2)
print(f"Original size: {csv_total_weight:.2f} MB")
dataset.columns = dataset.columns.str.strip()
dataset["ID_numeric"] = dataset["Transaction ID"].str.replace("TXN_", "").astype(int)
all_frames = [dataset.drop(columns="ID_numeric")]

multiplier = 480

print(f"Generating {multiplier} copy...")

for i in range(1, multiplier):
    temp = dataset
    new_ids = temp["ID_numeric"] + (i * 1_000_000)
    temp["Transaction ID"] = "TXN_" + new_ids.astype(str)
    all_frames.append(temp.drop(columns="ID_numeric"))

big_dataset = pd.concat(all_frames, ignore_index=True)
print(f"\n---Quantity of row: {len(big_dataset)}"
      f"\n---INFO:---")
big_dataset.info()
total_memory = big_dataset.memory_usage(deep=True).sum() / (1024**2)
print(f"\n---Memory usage: {total_memory:.2f} MB")
row_memory = big_dataset.memory_usage(deep=True).sum() / (len(big_dataset))
print(f"---Memory of one row: {row_memory:.2f} B")

class ProcessingData:
    def chunking(self, df: pd.DataFrame):
        chunk_size = 500_000
        batch_no = 1
        results = []

        for chunk in range(0, len(df), chunk_size):
            print(f"Processing chunk №{batch_no}")
            chunk = df.iloc[i:i+chunk_size].copy()
            print(f"Processing chunk {i} to {i + chunk_size}")

            clean_chunk = self.pipeline(chunk)
            results.append(clean_chunk)
        return pd.concat(results, ignore_index=True)

    def drop_duplicates(self, df: pd.DataFrame):
        df = df.drop_duplicates()
        return df

    def data_typing(self, df: pd.DataFrame):
        df = df.replace(to_replace=["ERROR", "UNKNOWN", "Unknown"], value=np.nan)

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
        for col in df.select_dtypes(include=np.number).columns:
            df[col] = df[col].fillna(df[col].median())

        for col in df.select_dtypes(include=["object", "category"]).columns:
            mode_series = df[col].mode()
            if not mode_series.empty:
                df[col] = df[col].fillna(mode_series[0])

        for col in df.select_dtypes(include=[np.datetime64, "datetimetz"]).columns:
            df[col] = df[col].ffill().bfill()

        return df

    def optimize_memory(self, df: pd.DataFrame):
        for col in df.select_dtypes(include=np.number).columns:
            df[col] = pd.to_numeric(arg=df[col], downcast='integer' if 'int' in str(df[col].dtype) else 'float')
        return df

    def iqr(self, df: pd.DataFrame):
        num_df = df.select_dtypes(include=np.number)

        Q1 = num_df.quantile(0.25)
        Q3 = num_df.quantile(0.75)
        IQR = Q3 - Q1

        for col in num_df.columns:
            condition = (df[col] < (Q1[col] - 1.5 * IQR[col])) | \
                        (df[col] > (Q3[col] + 1.5 * IQR[col]))

            df.loc[condition, col] = np.nan
        return df

    def z_score(self, df: pd.DataFrame):
        num_col = df.select_dtypes(include=np.number).columns
        df[num_col] = (df[num_col] - df[num_col].mean()) / df[num_col].std()
        return df

    def pipeline(self, df: pd.DataFrame):
        print("Data is being processed, it will take a few minutes...")
        df = (df.pipe(self.drop_duplicates)
              .pipe(self.data_typing)
              .pipe(self.missing_value)
              .pipe(self.optimize_memory)
              .pipe(self.iqr)
              .pipe(self.z_score)
              )
        return df

process = ProcessingData()
print(process.pipeline(big_dataset).head(50))