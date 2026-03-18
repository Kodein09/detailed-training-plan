# import pandas as pd
#
# #IQR
# data = pd.Series([1,4,5,8,10,92,129])
# Q1 = data.quantile(0.25)
# Q3 = data.quantile(0.75)
# IQR = Q3 - Q1
#
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
#
# print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
# print(f"Lower: {lower}, Upper: {upper}")
#
# outliers = data[(data < lower) | (data > upper)]
# print(f"Outliers: {outliers}", end='\n\n')
#
# #z-score
#
# data = pd.Series([30,50,60,90,300])
# mean = data.mean()
# std = data.std()
#
# z_scores = (data - mean) / std
# print(f"mean: {mean}, standard: {std}, z_scores: {z_scores}")
#
# outliers = data[z_scores.abs() > 3]
# print(f"Outliers: {outliers}")