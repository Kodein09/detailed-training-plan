import pandas as pd
import numpy as np

dataset = pd.DataFrame(data = {
    'Transaction ID': ['TXN_001', 'TXN_002', 'TXN_003', 'TXN_004', 'TXN_005', 'TXN_006', 'TXN_007', 'TXN_008', 'TXN_009', 'TXN_010'],
    'Item': ['Coffee', 'Cake', 'Coffee', 'Smoothie', 'Coffee', 'Tea', 'Coffee', 'Cookie', 'Cake', 'Coffee'],
    'Quantity': [2, 1, 1, 1, 500, 2, 1, 1, 2, 1],
    'Price Per Unit': [3.5, 5.0, 3.5, 6.0, 3.5, 2.5, 3.5, 1000.0, 5.0, 3.5],
    'Total Spent': ['7.0', '5.0', 'ERROR', '6.0', '1750.0', '5.0', '3.5', '1000.0', '10.0', '3.5'],
    'Transaction Date': ['2026-04-01', '2026-04-01', '2026-04-02', 'UNKNOWN', '2026-04-02', '2026-04-03', '2026-04-03', '2026-04-04', '2026-04-04', '2026-04-05']
})

class AutoDetectionAnomaly:
    def detect_outliers_iqr(self, df: pd.DataFrame, column: str):
        df_copy = df.copy()

        Q1 = df_copy[column].quantile(0.25)
        Q3 = df_copy[column].quantile(0.75)
        IQR = Q3 - Q1

        lower_outliers = Q1 - 1.5 * IQR
        upper_outliers = Q3 + 1.5 * IQR

        return (df_copy[column] < lower_outliers) | (df_copy[column] > upper_outliers)

    def detect_z_scores(self, df: pd.DataFrame, column: str, threshold=3):
        df_copy = df.copy()
        mean = df_copy[column].mean()
        std = df_copy[column].std()
        z_score = (df_copy[column] - mean) / std
        return np.abs(z_score) > threshold

auto_detect = AutoDetectionAnomaly()
print(f"Outliers: \n{auto_detect.detect_outliers_iqr(dataset, column='Quantity')}\n")
print(f"Z-Scores: \n{auto_detect.detect_z_scores(dataset, column='Quantity')}\n")
