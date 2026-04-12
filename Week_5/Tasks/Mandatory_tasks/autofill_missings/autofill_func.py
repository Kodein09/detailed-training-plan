import re

import pandas as pd
import numpy as np
from pydantic import BaseModel, field_validator, Field

pd.set_option("display.max_columns", None)
pd.set_option("display.max_row", None)
pd.set_option("display.width", None)

dataset = pd.read_csv('dirty_cafe_sales.csv')
# print(dataset.head(50))


class Validation(BaseModel):
    Transaction_ID: str = Field(validation_alias="Transaction ID", default=None)
    @field_validator("Transaction_ID")
    @classmethod
    def validate_id(cls, v):
        if not re.match(r"^[a-zA-Z0-9.-_]+$"):
            raise ValueError("Invalid Transaction ID")
        return v

class Imputation:
    def drop_duplicates(self, df):
        if df.empty:
            return pd.DataFrame

        df_copy = df.copy()
        return df_copy.drop_duplicates()

    def fix_types(self, df: pd.DataFrame):
        if df.empty:
            return df

        df_copy = df.copy()

        df_copy = df_copy.replace(to_replace=["ERROR", "UNKNOWN", "Unknown"], value=np.nan)

        for col in df_copy.columns:
            #int
            num_conv = pd.to_numeric(arg=df_copy[col], errors='coerce')
            if num_conv.notna().mean() > 0.6:
                df_copy[col] = num_conv

            #date
            date_conv = pd.to_datetime(arg=df_copy[col], format='%Y-%m-%d', errors='coerce')
            if date_conv.notna().mean() > 0.6:
                df_copy[col] = date_conv

        return df_copy

    def fill_missing(self, df: pd.DataFrame):
        df_copy = df.copy()

        num_cols = df_copy.select_dtypes(include=np.number).columns
        df_copy[num_cols] = df_copy[num_cols].fillna(df_copy[num_cols].median())

        date_cols = df_copy.select_dtypes(include=np.datetime64).columns
        df_copy[date_cols] = df_copy[date_cols].ffill().bfill()

        str_cols = df_copy.select_dtypes(include='object')
        for col in str_cols:
            most_frequent = df_copy[col].mode()
            if not most_frequent.empty:
                df_copy[col] = df_copy[col].fillna(value=most_frequent[0])
            else:
                df_copy[col].fillna(value="Unknown")

        return df_copy

    def validated_data(self, df: pd.DataFrame):
        df_copy = df.copy()

        valid_rows = []
        errors = []
        errors_count = 0
        for idx, row in df_copy.iterrows():
            try:
                validated_row = Validation(**row.to_dict())
                valid_rows.append(validated_row.model_dump())
            except Exception as e:
                errors_count += 1
                errors.append({"row": idx, "errors": str(e.errors())})
        return pd.DataFrame(valid_rows), errors

    def run_pipeline(self, df: pd.DataFrame):
        cleaned_df = (
            df.pipe(self.drop_duplicates)
              .pipe(self.fix_types)
              .pipe(self.fill_missing))

        return cleaned_df.head(50)


imp = Imputation()
print(imp.run_pipeline(dataset))
