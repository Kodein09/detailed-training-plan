import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification


X, y = make_classification(
    n_samples=100,
    n_features=5,
    n_informative=2,
    n_redundant=2,
    n_repeated=1,
    random_state=42
)

# theta = 3.0
# b = 0.0
#
# print(X)
# print(y)
#
# plt.figure(figsize=(10, 6))
# plt.scatter(X[:, 3], y, c='RoyalBlue', alpha=0.6, label='Classification Data')
#
# x = np.linspace(X[:, 3].min(), X[:, 3].max(), 100)
# z = theta * x + b
# S = 1 / (1 + np.exp(-z))
#
# plt.plot(x, S, c='maroon', linewidth=2, label='Sigmoid (Probability)')
# plt.title("Logistic Regression")
# plt.legend()
# plt.xlabel("x (features)")
# plt.ylabel("y (Parameters)")
# plt.grid(True, linestyle='--')
# plt.show()


theta = 2.0
b = -1.5
lmbd = 0.1

#
X_real = np.linspace(X[:, 2].min(), X[:, 2].max(), 100)
Z_real = theta * X_real + b
S = 1 / (1 + np.exp(-Z_real))
S = np.clip(S, 1e-15, 1-1e-15)

base_log_loss = -np.mean(y * np.log(S) + (1 - y) * np.log(1 - S))
l1_regularization = base_log_loss + lmbd * np.abs(theta)
print(f"Log loss: {base_log_loss:.1f}")
print(f"Error with regularization: {l1_regularization:.1f}")

x = np.linspace(X_real.min(), X_real.max(), 100)
z = theta * x + b
s = 1 / (1 + np.exp(-z))

plt.scatter(X_real, y, c='RoyalBlue', label='Classification Data')
plt.plot(x, s, c='maroon', label='Sigmoid function')
plt.title("Probability Logistic Regression")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle='--')
plt.show()