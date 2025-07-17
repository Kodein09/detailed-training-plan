import itertools

data = [10, 20, 30]

daily_data = list(zip(range(10), data))

for key, value in dict(daily_data).items():
    print(f"{key}: {value}")

print(daily_data)