import numpy as np

# 1. Create a 5x5 matrix of random integers between 1 and 50

matrix = np.random.randint(1, 51, size=(5,5))
print("Original Matrix:\n", matrix)

# 2. Replace all even numbers with 0

matrix[matrix % 2 == 0] = 0
print("\nMatrix with even numbers replaced by 0:\n", matrix)

# 3. Find the row with the highest sum

row_sums = matrix.sum(axis=1)
max_row_index = np.argmax(row_sums)
print("\nRow with the highest sum:", matrix[max_row_index])
