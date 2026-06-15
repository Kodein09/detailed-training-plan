# import numpy as np
#
# from sklearn.datasets import make_classification
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import cross_validate, StratifiedKFold, KFold
#
# model = LogisticRegression()
#
# scoring_metrics = ['accuracy', 'precision', 'recall']
#
# X, y = make_classification(n_samples=1000, n_features=100, random_state=20)
#
# cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
# cv_results = cross_validate(estimator=model, X=X, y=y,cv=cv_strategy, scoring=scoring_metrics)
#
# for i in range(5):
#     print(f"Accuracy: {cv_results['test_accuracy'][i] * 100:.0f}%")
#     print(f"Precision: {cv_results['test_precision'][i]* 100:.0f}%")
#     print(f"Recall: {cv_results['test_recall'][i] * 100:.0f}%")
#
# print("--- Среднее арифметическое ---")
# print(f"Mean Accuracy: {cv_results['test_accuracy'].mean() * 100:.0f}%")
# print(f"Mean Precision: {cv_results['test_precision'].mean() * 100:.0f}%")
# print(f"Mean Recall: {cv_results['test_recall'].mean() * 100:.0f}%")


import numpy as np
import pandas as pd
import sklearn.metrics
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit, cross_validate
from sklearn.metrics import get_scorer_names


# print(get_scorer_names())

dates = pd.date_range("13/06/2026", periods=100, freq='D')
df = pd.DataFrame(index=dates)

df['target'] = np.arange(100) + np.random.normal(0, 5, 100)

df['lag_1'] = df['target'].shift(1)
df['lag_2'] = df['target'].shift(2)

df = df.dropna()

X = df[['lag_1', 'lag_2']]
y = df['target']

print(f"DataFrame:\n{df}\n")

#init model
model = LinearRegression()

#metrics
scoring_metrics = ['neg_mean_absolute_error', 'neg_mean_squared_error', 'neg_root_mean_squared_error', 'r2']

#time series split для временных рядов, разбиваем на 5 последовательных шагов
cv_timeseries = TimeSeriesSplit(n_splits=5)

#cross validation
cv_result = cross_validate(estimator=model, X=X, y=y, cv=cv_timeseries, scoring=scoring_metrics)

for i in range(5):
    print(f"--- Step {i+1} ---")
    print(f"MAE: {abs(cv_result['test_neg_mean_absolute_error'][i]):.2f}")
    print(f"MSE: {abs(cv_result['test_neg_mean_squared_error'][i]):.2f}")
    print(f"RMSE: {abs(cv_result['test_neg_root_mean_squared_error'][i]):.2f}")
    print(f"R^2: {cv_result['test_r2'][i]:.2f}")


import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

X, y = make_regression(
    n_samples=100,   # Количество образцов.
    n_features=1,    # Количество признаков.
    n_informative=1,    # Количество признаковых, использованных для построения линейной модели, применяемой для
                        # генерации выходных данных.
    n_targets=1,    # Размерность вектора выходных данных 'y', связанного с выборкой, по умолчанию выходные данные
                    # представляют собой скаляр.
    noise=10,    # Стандартное отклонение Гауссового шума, приложенного к выходному сигналу.
    random_state=20
)

fig = plt.figure(figsize=(12, 10))

gs = fig.add_gridspec(nrows=2, ncols=2)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, :])

ax1.scatter(X, y, color='RoyalBlue')
ax1.set_title("Example of making regression")
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# Разделение данных на обучающие и тестовые, размер для тестовых данных составляет 33% от всех данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=10)

# инициализация модели регрессии деревьев
tree = DecisionTreeRegressor()

# Обучение модели тренировочными данными
tree.fit(X_train, y_train)

# Предсказывание модели
pred_train_overfitting = tree.predict(X_train)
mse_train_overfitting = mean_squared_error(y_train, pred_train_overfitting)
print(f"MSE на обучении: {mse_train_overfitting:.2f}")

ax2.scatter(X_train, y_train, color='steelblue', alpha=1, label="Train data")
ax2.set_title("Tree Regression Overfitting")

sort_idx = np.argsort(X_train.flatten())
X_sort = X_train[sort_idx]
pred_sort = pred_train_overfitting[sort_idx]
ax2.plot(X_sort, pred_sort, color="Red", alpha=0.5, linewidth=2, label="Decision Tree")
ax2.set_title("Tree Regression Overfitting on train data")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.legend()

pred_test_overitting = tree.predict(X_test)
mse_test_overfitting = mean_squared_error(y_test, pred_test_overitting)
print(f"MSE на тесте: {mse_test_overfitting:.2f}")

sort_idx = np.argsort(X_test.flatten())
X_sort = X_test[sort_idx]
pred_sort = pred_test_overitting[sort_idx]

ax3.scatter(X_test, y_test, color='Blue', label='Test')
ax3.scatter(X_sort, pred_sort, color='Red', label='Prediction')
ax3.set_title("Tree Regression Overfitting on test data")

ax3.plot(X_sort, pred_sort, color='Red', alpha=0.6, linewidth=1, label='Actual')
ax3.set_title("Prediction Regression Overfitting on tested data")
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.legend()

plt.tight_layout()
plt.show()
