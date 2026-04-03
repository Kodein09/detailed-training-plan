import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

from IPython.core.pylabtools import figsize
from pydantic import BaseModel, field_validator, model_validator, Field

pd.set_option('display.max_row', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

dataset = pd.read_csv("dirty_cafe_sales.csv")

class Validation(BaseModel):
    Transaction_ID: str = Field(validation_alias="Transaction ID")
    Item: str
    Quantity: int
    Price_per_unit: float | None = Field(validation_alias="Price Per Unit", default=None)
    Total_spent: float | None = Field(validation_alias="Total Spent", default=None)
    Payment_method: str = Field(validation_alias="Payment Method", default=None)
    Location: str
    Transaction_date: datetime | None = Field(validation_alias="Transaction Date", default=None)

    @model_validator(mode='after')
    def check_total(self):
        if (
            self.Quantity is not None and
            self.Price_per_unit is not None and
            self.Total_spent is not None
        ):
            if abs(self.Quantity * self.Price_per_unit - self.Total_spent) > 1e-6:
                raise ValueError("Total Spent mismatch")
        return self

    @field_validator("Transaction_ID")
    @classmethod
    def validate_transaction_id(cls, v):
        if not re.match(r"^[a-zA-Z0-9_\-]+$", v):
            raise ValueError("Invalid Transaction ID format")
        return v

    @field_validator("Quantity", "Price_per_unit", "Total_spent")
    @classmethod
    def validate_positive(cls, v):
        if v is not None and v < 0:
            raise ValueError("Value must be positive")
        return v

class Dashboard:
    def __init__(self):
        self.stats = {"Duplicated_value": 0, "Missing_value": 0, "Validation_errors": 0, "Error_counts": 0}

    def clean_data(self, df: pd.DataFrame):
        df_copy = df.copy()

        #Remove duplicates
        self.stats["Duplicated_value"] = df.duplicated().sum()
        df_copy = df_copy.drop_duplicates()

        #Missing values
        df_copy = df_copy.replace(["ERROR", "UNKNOWN", "Unknown"], np.nan)
        self.stats["Missing_value"] = df_copy.isnull().sum().sum()

        #Data types
        for col in df_copy.columns:
            num_conv = pd.to_numeric(arg=df_copy[col], errors='coerce')
            if num_conv.notna().mean() > 0.6:
                df_copy[col] = num_conv

            date_conv = pd.to_datetime(arg=df_copy[col], format='%Y-%m-%d', errors='coerce')
            if date_conv.notna().mean() > 0.6:
                df_copy[col] = date_conv

        #Int
        num_cols = df_copy.select_dtypes(include=np.number).columns
        df_copy[num_cols] = df_copy[num_cols].fillna(df_copy[num_cols].median())

        #Str
        str_cols = df_copy.select_dtypes(include='object').columns
        for col in str_cols:
            most_frequent = df_copy[col].mode()
            if not most_frequent.empty:
                df_copy[col] = df_copy[col].fillna(value=most_frequent[0])
            else:
                df_copy[col] = df_copy[col].fillna(value="Unknown")

        #Date
        date_cols = df_copy.select_dtypes(include=np.datetime64).columns
        df_copy[date_cols] = df_copy[date_cols].ffill()

        return df_copy

    def validate_data(self, df: pd.DataFrame):
        valid_rows = []
        errors = []
        error_counts = 0

        for idx, row in df.iterrows():
            try:
                validated_row = Validation(**row.to_dict())
                valid_rows.append(validated_row.model_dump())
            except Exception as e:
                errors.append({"row": idx, "errors": e.errors()})
                error_counts += 1

        self.stats["Validation_errors"] = len(errors)
        self.stats["Error_counts"] = error_counts
        return pd.DataFrame(data=valid_rows), errors

    def visualization_data(self, df: pd.DataFrame):
        if df.empty:
            print("No data for visualization")
            return None

        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

        #First plot
        df["Item"].value_counts().head(10).plot(kind='bar', ax=axes[0, 0])
        axes[0, 0].set_title("Top 10 Items")

        #Second plot
        axes[0, 1].hist(df["Quantity"], bins=20, color='orange')
        axes[0, 1].set_title("Quantity")

        #Third plot
        axes[1, 0].boxplot(df["Price_per_unit"])
        axes[1, 0].set_title("Price per Unit")

        #Fourth plot
        axes[1, 1].plot(df["Total_spent"].head(100))
        axes[1, 1].set_title("Total Spent (First 100)")

        plt.tight_layout()
        plt.show()
        return axes

    def run_pipeline(self, df: pd.DataFrame):
        cleaned_data = self.clean_data(df)
        validated_data, errors = self.validate_data(cleaned_data)
        dashboard_data = self.visualization_data(validated_data)

        if validated_data.empty:
            print(f"Error founded: {len(errors)}")

        return validated_data.head(50), self.stats

    # def clean_data(self, df: pd.DataFrame):
    #     df_copy = df.copy()
    #
    #     #Remove duplicates
    #     initial_row = len(df)
    #     self.stats["Duplicated_value"] = initial_row - len(df_copy)
    #     df_copy = df_copy.drop_duplicates()
    #
    #     #Replace known invalid values
    #     df_copy = df_copy.replace(["ERROR", "UNKNOWN", "Unknown"], np.nan)
    #
    #     #Count missing
    #     self.stats["Missing_value"] = df_copy.isnull().sum().sum()
    #
    #     for col in df_copy.columns:
    #         converted = pd.to_numeric(arg=df_copy[col], errors='coerce')
    #         if converted.notna().mean() > 0.7:
    #             df_copy[col] = converted
    #
    #     for col in df_copy.columns:
    #         converted = pd.to_datetime(arg=df_copy[col], format='%Y-%m-%d', errors='coerce')
    #         if converted.notna().mean() > 0.7:
    #             df_copy[col] = converted
    #
    #     #Numeric
    #     num_cols = df_copy.select_dtypes(include=np.number).columns
    #     df_copy[num_cols] = df_copy[num_cols].apply(lambda x: x.fillna(x.median()))
    #
    #     #String
    #     str_cols = df_copy.select_dtypes(include='object').columns
    #     df_copy[str_cols] = df_copy[str_cols].fillna("Unknown")
    #
    #     #Datetime
    #     dt_cols = df_copy.select_dtypes(include=np.datetime64).columns
    #     df_copy[dt_cols] = df_copy[dt_cols].ffill()
    #
    #     return df_copy


    # def clean_data(self, df: pd.DataFrame):
    #     df_copy = df.copy()
    #     initial_rows = len(df)
    #
    #     #duplicated value
    #     df_copy.drop_duplicates(inplace=True)
    #     self.stats["Duplicated_value"] = initial_rows - len(df_copy)
    #
    #     #missing value
    #     df_copy.replace(["ERROR", "UNKNOWN"], np.nan, inplace=True)
    #     self.stats["Missing_value"] = df_copy.isnull().sum().sum()
    #
    #     numeric_column = df_copy.select_dtypes(include=np.number).columns
    #     df_copy[numeric_column] = df_copy[numeric_column].fillna(df_copy[numeric_column].median())
    #
    #     string_column = df_copy.select_dtypes(include='object').columns
    #     df_copy[string_column] = df_copy[string_column].fillna('Unknown')
    #
    #     for col in df_copy.columns:
    #         if np.issubdtype(df_copy[col].dtype, np.number):
    #             df_copy[col] = pd.to_numeric(df_copy[col], errors='coerce')
    #         elif np.issubdtype(df_copy[col].dtype, 'object'):
    #             df_copy[col] = df_copy[col].fillna(value='Unknown')
    #         elif np.issubdtype(df_copy[col].dtype, np.datetime64):
    #             df_copy[col] = pd.to_datetime(df_copy[col], errors='coerce')
    #             df_copy[col] = df_copy[col].bfill()
    #
    #     return df_copy

dash = Dashboard()
print(dash.run_pipeline(dataset))