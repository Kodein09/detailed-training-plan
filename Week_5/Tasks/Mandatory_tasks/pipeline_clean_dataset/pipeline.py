import re
import numpy as np
import pandas as pd

from typing import Optional, Dict, Any
from pydantic import BaseModel, field_validator, ValidationError

pd.set_option('display.max_row', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# df = pd.read_csv('synthetic_text_cleaning_realworld.csv')
# print(df, '\n')


## Validate Data
# class DataValidator(BaseModel):
#     name: str
#     age: Optional[int] = None
#     email: Optional[str] = None
#     salary: Optional[float] = None
#
#     @field_validator('age')
#     @classmethod
#     def validate_age(cls, age):
#         if age is not None and (age < 0 or age > 120):
#             raise ValueError("Age must be between 0 and 120")
#         return age
#
#     @field_validator('email')
#     @classmethod
#     def validate_email(cls, email):
#         if email is None:
#             return email
#
#         pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
#
#         if not re.match(pattern, email):
#             raise ValueError("Invalid email format")
#
#         return email
#
#     @field_validator('email')
#     @classmethod
#     def validate_email(cls, email):
#         if email is None:
#             return email
#         elif re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
#             raise ValueError("")
#         return email
#
#
# # Pipeline
# class Pipeline:
#     def __init__(self):
#         self.cleaning_stats = {"duplicates_removed": 0, "nulls_handled": 0, "validation_errors": 0}
#
#     def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
#         initial_rows = len(df)
#
#         #Remove duplicates
#         df.drop_duplicates(inplace=True)
#         self.cleaning_stats["duplicates_removed"] = initial_rows - len(df)
#
#         #Handle missing values
#         numeric_columns = df.select_dtypes(include=[np.number]).columns
#         df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
#
#         string_columns = df.select_dtypes(include='object').columns
#         df[string_columns] = df[string_columns].fillna('Unknown')
#
#         return df
#
#     def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
#         valid_rows = []
#         errors = []
#
#         for idx, row in df.iterrows():
#             try:
#                 validated_row = DataValidator(**row.to_dict())
#                 valid_rows.append(validated_row.model_dump())
#             except ValidationError as e:
#                 errors.append({'row': idx, 'errors': e.errors})
#
#         self.cleaning_stats['validation_errors'] = len(errors)
#         return pd.DataFrame(valid_rows), errors
#
#     def process(self, df: pd.DataFrame) -> Dict[str, Any]:
#         cleaned_df = self.clean_data(df.copy())
#         validated_df, validation_errors = self.validate_data(cleaned_df)
#
#         return {
#             "cleaned_data": cleaned_df,
#             "validation_errors": validation_errors,
#             "stats": self.cleaning_stats
#         }
#
# sample_data = pd.DataFrame({
#     'name': ['Tara Jamison', 'Jane Smith', 'Lucy Lee', None, 'Clara Clark','Jane Smith'],
#     'age': [25, -5, 25, 35, 150,-5],
#     'email': ['taraj@email.com', 'invalid-email', 'lucy@email.com', 'jane@email.com', 'clara@email.com','invalid-email'],
#     'salary': [50000, 60000, 50000, None, 75000,60000]
# })
#
# pipeline = Pipeline()
# print(pipeline.process(sample_data))



class CompletePipeline:
    def __init__(self):
        self.cleaning_stats = {"Duplicates_removed": 0, "Validation_errors": 0, "Nulls_handled": 0}

    @staticmethod
    def data_profiling(df: pd.DataFrame):
        return df.dtypes

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        initial_rows = len(df)

        #1. Remove duplicates
        df.drop_duplicates(inplace=True)
        self.cleaning_stats["Duplicates_removed"] = initial_rows - len(df)

        #2. Handle nulls
        self.cleaning_stats["Nulls_handled"] = df.isnull().sum().sum()

        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].fillna(value=df[numeric_cols].median())

        string_cols = df.select_dtypes(include='object').columns
        df[string_cols] = df[string_cols].fillna(value='Unknown')

        #3. Conditional filtering
        df = df[(df["age"] > 0) & (df["age"] <= 120)]
        # df = df[(df['age'] <= 0) | (df['age'] > 120)]

        self.cleaning_stats["Duplicates_removed"] = initial_rows - len(df)

        return df

    def validate_data(self, df: pd.DataFrame):
        valid_rows = []
        errors = []

        for idx, row in df.iterrows():
            try:
                validated_row = ValidationData(**row.to_dict())
                valid_rows.append(validated_row.model_dump())
            except Exception as e:
                errors.append({"row": idx, "errors": str(e.errors())})
                self.cleaning_stats["Validation_errors"] += 1

        self.cleaning_stats["Validation_errors"] = len(errors)
        return pd.DataFrame(valid_rows), errors

    def process(self, df: pd.DataFrame):
        cleaned_df = self.clean_data(df.copy())
        validated_df = self.validate_data(cleaned_df)

        return {
            "Cleaned": cleaned_df,
            "Validation_errors": validated_df,
            "Stats": self.cleaning_stats
        }

class ValidationData(BaseModel):
    name: str
    age: Optional[int] = None
    email: Optional[str] = None
    salary: Optional[float] = None

    @field_validator('name')
    @classmethod
    def validate_name(cls, name):
        pattern = r"^[a-zA-Z0-9._%+-]+"
        if not re.match(pattern, name):
            raise ValidationError("Invalid name")
        elif len(name) < 1 or len(name) > 100:
            raise ValueError("Name length must be 0-100 characters")
        return name

    @field_validator('age')
    @classmethod
    def validate_age(cls, age):
        if age is not None and (age <= 0 or age > 120):
            raise ValueError("Age must be between 1-120")
        return age

    @field_validator('email')
    @classmethod
    def validate_email(cls, email):
        pattern = r"^[a-zA-Z0-9._%+-]+\@[a-zA-Z]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise ValueError("Invalid email")
        return email

    @field_validator('salary')
    @classmethod
    def validate_salary(cls, salary):
        if salary <= 0 or salary >= 100_000:
            raise ValueError("Invalid salary")
        return salary

sample_data = pd.DataFrame({
    'name': ['Tara Jamison', 'Jane Smith', 'Lucy Lee', None, 'Clara Clark','Jane Smith'],
    'age': [25, -5, 25, 35, 150,-5],
    'email': ['taraj@email.com', 'invalid-email', 'lucy@email.com', 'jane@email.com', 'clara@email.com','invalid-email'],
    'salary': [50000, 60000, 50000, None, 75000,60000]
})

pipeline = CompletePipeline()
print(pipeline.data_profiling(sample_data), '\n')

result = pipeline.process(sample_data)
print(f"Cleaned data:\n{result}")
