import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# создаём случайную матрицу 5x5
data = np.random.rand(5, 5)

sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("Heatmap Example")
plt.show()

import pandas as pd

df = pd.DataFrame({
    "age": [20, 22, 25, 30, 40, 50],
    "income": [2000, 2500, 3000, 4000, 5000, 6000],
    "score": [60, 65, 70, 80, 90, 95]
})

corr = df.corr()  # корреляционная матрица
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

tips = sns.load_dataset("tips")  # встроенный датасет

sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Boxplot Example")
plt.show()