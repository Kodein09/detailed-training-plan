import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression


model = LinearRegression()

X, y = make_regression(
    n_samples=100,
    n_features=1,
    n_informative=1,
    noise=10,
    random_state=42
)

print(f"X:\n{X}\n"
      f"y:\n{y}\n")

fig = plt.figure(figsize=(12, 10))
plt.scatter(X, y, c='RoyalBlue', alpha=0.6, label="Data")
plt.title("Visualization data")
plt.xlabel('feature')
plt.ylabel('target')
plt.legend()
plt.show()

model.fit(X, y)
print(f"Coefficient: {model.coef_}")
print(f"Intercept: {model.intercept_}")

model_a = model.coef_[0]
model_b = model.intercept_

print(f"Model of a: {model_a}")
print(f"Model of b: {model_b}")

x = np.arange(-3, 3)
linear_model = model_a * x + model_b
plt.plot(x, linear_model, linewidth=2, c='maroon', label=f'linear model= {model_a:.2f}x + {model_b:.2f}')
plt.scatter(X, y, alpha=0.6, label='Data', c='RoyalBlue')
plt.plot([0, 1], [model_b, model_b], 'r', linewidth=3, label='Angle',)
plt.plot([1, 1], [model_b, model_b+model_a], 'b', linewidth=3, label='Shift')
plt.grid()
plt.xlabel('feature')
plt.ylabel('target')
plt.legend()
plt.show()