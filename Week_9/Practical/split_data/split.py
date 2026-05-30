import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.DataFrame({
    'Name': ['Audi', 'Toyota', 'Chevrolet'],
    'Model': ['RS7', 'GR GT', 'Camaro'],
    'Year': [1940, 1943, 1967],
    'Acceleration': [4, 3, 9]
})

X = dataset[['Year']]
y = dataset['Acceleration']

print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(f"---Original Dataset---\n{dataset}\n")
print(f"---X_test---\n{X_test}\n")
print(f"---y_test---\n{y_test}\n")
print(f"---X_train---\n{X_train}\n")
print(f"---y_train---\n{y_train}\n")

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("---MODEL ANSWER---")
print(f"Car from test-choose:\n{X_test}\n")
print(f"MODEL PREDICTIONS: {predictions}")
print(f"CORRECT ANSWER: {y_test.values}")