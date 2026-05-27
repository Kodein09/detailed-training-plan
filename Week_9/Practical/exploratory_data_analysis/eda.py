# EDA корреляция - статистический показатель линейной связи между двумя переменными. Корреляция помогает находить
# скрытые взаимосвязи, определять и выявлять мультиколлинеарность (сильную связь между независимыми признаками).
# Матрица корреляции представляет собой таблицу, в которой показывается взаимосвязь между каждой парой
# числовых признаков в датасете.
# При +1(положительный) прямая связь: при росте одного числового признака другой также возрастает.
# При -1(Отрицательный) обратная связь: при росте одного числового признака, второй признак убывает.
# При 0(Нейтрально) или ближе к 0 линейная связь отсутствует.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

df = pd.read_csv("../train.csv")

#CORRELATION MATRIX
# numeric_df = df.select_dtypes(include=np.number)
#
# corr_matrix = numeric_df.corr()
#
# sns.heatmap(
#     corr_matrix,
#     cmap='coolwarm',
#     annot=True,
#     fmt='.2f',
#     linewidths=1,
#     linecolor='black',
#     robust=True,
#     square=True
# )
#
# print(df.info())
# plt.title("Correlation Matrix")
# plt.show()



#DISTRIBUTON
# fig, axes = plt.subplots(1,2, figsize=(15, 5))
# print(fig)
# print(axes)
#
# sns.histplot(df['Age'].dropna(), kde=True, ax=axes[0], color='skyblue')
# axes[0].set_title("Age Distribution")
# axes[0].set_xlabel('Age')
#
# sns.histplot(df['Fare'], kde=True, ax=axes[1], color='RoyalBlue')
# axes[1].set_title("Ticket Cost Distribution")
# axes[1].set_xlabel('Fare')
#
# plt.tight_layout()
# plt.show()



#Outliers
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

sns.boxplot(df['Age'], ax=axes[0], color='RoyalBlue')
axes[0].set_title("Age Outliers")
axes[0].set_xlabel('Age')

sns.boxplot(df['Fare'], ax=axes[1], color='steelblue')
axes[1].set_title("Fare Outliers")
axes[1].set_xlabel('Fare')

plt.tight_layout()
plt.show()