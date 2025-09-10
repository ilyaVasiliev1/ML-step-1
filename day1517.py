import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

arr = np.arange(1, 101)
print(arr)

arr = np.linspace(0, 1, 5)
print(arr)

arr = np.zeros(5)
print(arr)

arr = np.ones((2, 3))
print(arr)

arr = np.eye(3)
print(arr)

arr = np.arange(1,13)
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)

arr = np.arange(1,13)
print(arr.reshape(-1, 4))
print(arr.reshape(-1, 6))


data = np.array([1, 2, 3, 4, 5])
print("sum:", data.sum())
print("min:", data.min())
print("max:", data.max())
print("mean:", data.mean())
print("std:", data.std())
print("argmin:", data.argmin())
print("argmax:", data.argmax())


matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(matrix.mean())        # среднее всех элементов = 5.0
print(matrix.mean(axis=0))  # среднее по столбцам → [4. 5. 6.]
print(matrix.mean(axis=1))  # среднее по строкам   → [2. 5. 8.]