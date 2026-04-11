import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

dataset = pd.read_csv("Customer_Transactions.csv")
df_list = []

for i in range(20):
    temp = dataset.copy()
    temp["customer_id"] = temp["customer_id"] + i * 10000
    df_list.append(temp)

scaling_df = pd.concat(df_list, ignore_index=True)
# print(scaling_df.head(40))
# print(scaling_df.tail(20))
print(f"Scale shape: {scaling_df.shape}")

#save dataset
scaling_df.to_csv("big_dataset.csv", index=False)

dtypes = {"id": "int16", "age": "int16", "gender": "str", "county": "str", "annual_incode": "float32", "spending_score": "int32"}
big_dataset = pd.read_csv(
    filepath_or_buffer="big_dataset.csv",
    dtype=dtypes,
    usecols=["customer_id", "age", "gender", "country", "annual_income", "spending_score", "membership_years",
             "website_visits_per_month", "cart_abandon_rate", "churned", "feedback_text", "last_purchase_date"]
)


class ScalingBigData:
    def __init__(self):
        self.memory = []

    def clean_data(self, df: pd.DataFrame):
        # check memory
        print(df.info())
        print(df.memory_usage(deep=True))

        df_copy = df.copy()

        #dupl data
        df_copy = df_copy.drop_duplicates()

        #types data
        for col in df_copy.columns:
            num_conv= pd.to_numeric(arg=df_copy[col], errors='coerce', downcast='integer')
            if num_conv.notna().mean() > 0.6:
                df_copy[col] = num_conv

        for col in df_copy.columns:
            date_conv = pd.to_datetime(arg=df_copy[col], format='%Y-%m-%d', errors='coerce')
            if date_conv.notna().mean() > 0.6:
                df_copy[col] = date_conv

        #missing data
        str_col = df_copy.select_dtypes(include='object')
        for col in str_col:
            most_frequent = df_copy[col].mode()
            if not most_frequent.empty:
                df_copy[col] = df_copy.fillna(most_frequent[0])

        df_copy = df_copy.replace(to_replace="Unknown", value=np.nan)

        num_col = df_copy.select_dtypes(include=np.number).columns
        df_copy[num_col] = df_copy[num_col].fillna(df_copy[num_col].median())

        date_col = df_copy.select_dtypes(include=np.datetime64).columns
        df_copy[date_col] = df_copy[date_col].ffill().bfill()

        return df_copy

    def scale_zscore(self, df: pd.DataFrame):
        num_cols = df.select_dtypes(include=np.number).columns
        df[num_cols] = (df[num_cols] - df[num_cols].mean()) / df[num_cols].std()
        return df

    def process_chunks(self, file_path):
        result = []
        #chunking
        for chunk in pd.read_csv(file_path, chunksize=10_000):
            chunk = self.clean_data(chunk)
            chunk = self.scale_zscore(chunk)
            result.append(chunk)

        return pd.concat(result, ignore_index=True)


    def run_pipeline(self, df: pd.DataFrame):
        scaled_df = (df.pipe(self.clean_data).pipe(self.scale_zscore))

        before = df.memory_usage(deep=True).sum()
        after = scaled_df.memory_usage(deep=True).sum()

        return (f"\n-----Before -> {before / 1024**2:.2f} MB\n"
                f"\n-----After -> {after / 1024**2:.2f} MB\n"
                f"\nSCALED DATAFRAME:\n{scaled_df.head(50)}")

# scale = ScalingBigData()
# print(scale.run_pipeline(big_dataset))


# df = pd.DataFrame({'Name': ['Alice', 'Bob'],
#                    'Age': [25, 30],
#                    'Location': ['Seattle', 'New York']})
# print(df)
# print('COLUMNS:', df.columns)
# print('INDEX:', df.index)
