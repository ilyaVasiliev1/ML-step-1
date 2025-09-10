import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)
print(s.values)
print(s.index)

data = {
    "Name": ["Alice", "James", "Bob"],
    "Age": [25, 30, 35],
    "City": ["Moscow", "China", "Brasil"]
}

df = pd.DataFrame(data)
print(df)
print("===")
print(df.shape)
print("===")
print(df.columns)
print("===")
print(df["Age"])
print("===")
print(df[["Name", "City"]])
print("===")
print(df.iloc[1])
print("===")
print(df.loc[2, "Name"])

df = pd.read_csv("titanic.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())

adults = df[df["Age"] > 30]
women = df[df["Sex"] == "female"]
mens_1st_class = df[(df["Sex"] == "male") & (df["Pclass"] == 1)]
print(mens_1st_class.head())

# & = AND
# | = OR
# ~ = NOT

print(df.loc[0, "Name"])   # имя пассажира с индексом 0
print(df.iloc[0, 3])       # тоже имя, но по позиции

print(df.sort_values("Age", ascending=True).head())

#save df
adults.to_csv("adults.csv", index=False)