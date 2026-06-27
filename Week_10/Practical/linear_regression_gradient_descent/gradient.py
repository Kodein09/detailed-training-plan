import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression


# X, y = make_regression(
#     n_samples=100,
#     n_features=1,
#     n_informative=1,
#     noise=10,
#     random_state=42
# )
#
# model = LinearRegression()
#
# model.fit(X, y)
#
#
# def func(x):
#     return x ** 2
#
# def gr_func(x):
#     return 2 * x
# #
# # start_point = 5
# #
# X = np.linspace(-10, 10, 20)
# Y = func(X)
#
# plt.figure(figsize=(16, 6))
# plt.plot(X, Y, 'r', label="Y(X)")
# plt.plot(start_point, func(start_point), '*b', label='Start')
#
# grad = gr_func(start_point)
# learning_rate = 0.1
# next_point_1 = start_point - learning_rate * grad
# plt.plot([start_point, next_point_1], func(np.array([start_point, next_point_1])), '--*g', label='antigrad')
#
# plt.legend()
# plt.grid()
# plt.show()


# start_point = 5
# next_point = start_point
# learn_rate = 0.1
#
# x = []
# x.append(next_point)
#
# plt.figure(figsize=(16, 6))
# plt.plot(X, Y, 'r', label='Y(X)')
#
#
# for i in range(10):
#     current_point = next_point
#
#     next_point = current_point - learn_rate * (2 * current_point)
#     x.append(next_point)
#     print(f"Iteration: {i}, "
#           f"Current point: {current_point}, Next point: {next_point}")
#
# x_grad = np.array(x)
# plt.plot(x_grad, x_grad**2, '-*g', label='Gradient Descent')
# plt.grid()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()


# class LRGD:
#     def __init__(self):
#         self.X, self.y = make_regression(
#             n_samples=100,
#             n_features=1,
#             n_informative=1,
#             noise=10,
#             random_state=12
#         )
#         self.X = self.X.ravel()
#         self.k = 0.0
#         self.b = 0.0
#         self.lr = 0.01
#
#     def fit(self, epochs=100):
#         n = len(self.X)
#
#         for i in range(epochs):
#             y_pred = self.k * self.X + self.b
#             error = y_pred - self.y
#
#             grad_k = (1/n) * np.sum(error * self.X)
#             grad_b = (1/n) * np.sum(error)
#
#             self.k = self.k - self.lr * grad_k
#             self.b = self.b - self.lr * grad_b
#
#     def plot_result(self):
#         plt.scatter(self.X, self.y, c='RoyalBlue', alpha=0.6, label='Data', s=50)
#
#         x_line = np.linspace(self.X.min(), self.X.max(), 100)
#         y_line = self.k * x_line + self.b
#
#         plt.plot(x_line, y_line, 'r-', linewidth=3, label=f"Model: {self.k:.2f}x + {self.b:.2f}")
#
#         plt.title("Linear Regression via Gradient Descent")
#         plt.xlabel('x')
#         plt.ylabel('y')
#         plt.legend()
#         plt.grid()
#         plt.show()
#
# model = LRGD()
# model.fit(epochs=500)
# model.plot_result()


# salaries = [50, 45, 55, 48, 52, 50, 47, 53, 49, 1000]
#
# p_50 = np.percentile(salaries, 50)
# print(f"Percentile of 50-th: {p_50}")
# p_20 = np.percentile(salaries, 20, method='nearest')
# print(f"Percentile of 20-th: {p_20}")


# X = np.array([[1], [2], [3]])
# y = np.array([1, 3, 5])
#
# model = LinearRegression()
# model.fit(X, y)
# print(f"Model coef: {model.coef_[0]:.1f}, intercept: {model.intercept_:.1f}\n"
#       f"Formula of linear function: {model.coef_[0]:.0f}x{model.intercept_:.0f}")
#
# k = model.coef_[0]
# b = model.intercept_
#
# plt.figure(figsize=(12, 6))
# plt.scatter(X, y, alpha=0.8, c='RoyalBlue', s=100, zorder=5)
#
# x_line = np.linspace(X.min(), X.max(), 20)
# y_line = k * x_line + b
#
# plt.plot(x_line, y_line, c='crimson', linewidth=3, label=f'y={k:.0f}x{b:+.0f}')
# plt.title("Visualization of Linear Regression")
# plt.xlabel("x (Independent variable)")
# plt.ylabel("y (Dependent variable)")
# plt.legend()
# plt.grid()
# plt.show()

#Logic under fit()
# for i in X:
#     print(f"{model.coef_[0]:.0f}*{i[0]}{model.intercept_:.0f}={model.coef_[0]*i[0]+model.intercept_:.0f}")


# X, y = make_regression(
#       n_samples=100,
#       n_features=1,
#       n_informative=1,
#       noise=10,
#       random_state=42
# )
#
# k = 0.0
# b = 0.0
# lr = 0.1
# ep = 1000
#
# X_flat = X.flatten()
# print(X_flat)
#
# for epoch in range(ep):
#       n = len(X_flat)
#
#       #Делаем прогноз для всех точек сразу
#       y_pred = k * X_flat + b
#
#       #Находим разность ошибки между действительными данными и спрогнозированными данными
#       error = y_pred - y
#
#       #Антиградиент, считаем указатели направления(градиенты) наклона и сдвига
#       grad_k = (2/n)*np.sum(error * X_flat) #Среднее значение от перемножения ошибки на x
#       grad_b = (2/n)*np.sum(error) #Среднее значение ошибки
#
#       #Делаем шаг в сторону уменьшения ошибки
#       k = k - lr * grad_k
#       b = b - lr * grad_b
#
#
# plt.scatter(X, y, alpha=0.7, c='RoyalBlue', label='Data')
#
# x_line = np.linspace(X.min(), X.max())
# y_line = k * x_line + b
#
# plt.plot(x_line, y_line, c='r', label=f'y={k:.0f}x{b:+.0f}')
# plt.title("Linear Regression")
# plt.xlabel('x (Independent data)')
# plt.ylabel('y (Dependent data)')
# plt.grid()
# plt.legend()
# plt.show()


np.random.seed(42)
study_time = np.random.uniform(10, 50, 100)

k = 1.2
b = 20

base_score = k * study_time + b

noise = np.random.normal(loc=0, scale=7, size=100)

score = np.clip(base_score + noise, 0, 100)

print(f"Study time:\n{study_time}\n"
      f"Score:\n{score}")

plt.scatter(study_time, score, c='RoyalBlue', alpha=0.6)
plt.title("Exam Results")
plt.xlabel("Study Time")
plt.ylabel('Score')
plt.grid(linestyle='--')
plt.show()