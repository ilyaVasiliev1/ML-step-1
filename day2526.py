import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]



plt.plot(x, y, label="y = 2x", color = "blue", linestyle = "--", marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Пример линейного графика")
plt.legend()
plt.show()


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [55, 60, 65, 60, 55, 50, 45, 40, 100]

plt.scatter(x, y, color="red", alpha=1, marker="x")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter plot")
plt.show()

categories = ["A", "B", "C", "D"]
values = [3, 7, 2, 5]

# plt.barh(categories, values)
plt.bar(categories, values, color="green")
plt.title("Bar chart")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()

import numpy as np

data = np.random.randn(1000)  # 1000 случайных чисел (нормальное распределение)

plt.hist(data, bins=30, color="purple", alpha=0.7, edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()