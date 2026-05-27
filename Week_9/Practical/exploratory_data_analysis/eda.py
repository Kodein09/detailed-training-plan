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

df = pd.read_csv("../train.csv")

numeric_df = df.select_dtypes(include=np.number)

corr_matrix = numeric_df.corr()

sns.heatmap(
    corr_matrix,
    cmap='coolwarm',
    annot=True,
    fmt='.2f',
    linewidths=1,
    linecolor='black',
    robust=True,
    square=True
)

print(df.info())
plt.title("Correlation Matrix")
plt.show()
