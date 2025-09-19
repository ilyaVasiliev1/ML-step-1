import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Sex": ["female", "male", "male", "female"],
    "Age": [25, 30, 35, 28]
}

df = pd.DataFrame(data=data)

# print(df.groupby("Sex")["Age"].mean())
# print(df.groupby("Sex")["Age"].agg(["mean", "min", "max", "count"]))
# print(df.groupby(["Sex", "Name"])["Age"].mean())

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Income": [5000, 7000, 6000]
})

# print(df.sort_values("Income", ascending=True).head(5)) #ascending=False → сортировка по убыванию.



users = pd.DataFrame({
    "user_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "user_id": [1, 2, 2],
    "amount": [250, 400, 300]
})

df = pd.merge(users, orders, on="user_id", how="inner")
print(df)

# inner (по умолчанию) → только совпадения.
# left → все строки из левой таблицы + совпадения.
# right → все строки из правой.
# outer → объединение всех, где нет значений → NaN.