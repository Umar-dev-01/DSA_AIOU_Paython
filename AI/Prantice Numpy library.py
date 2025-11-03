

# 1. Create and Display an Array
arr1 = np.arange(10)
print("1D Array (0–9):", arr1)

# 2. Create a 2D Array
arr2 = np.arange(1, 10).reshape(3, 3)
print("\n3x3 Array:\n", arr2)
print("Shape:", arr2.shape)

# 3. Zeros, Ones, and Identity Matrix
zeros_arr = np.zeros((4, 4))
ones_arr = np.ones((3, 3))
identity_arr = np.eye(5)
print("\n4x4 Zeros Array:\n", zeros_arr)
print("\n3x3 Ones Array:\n", ones_arr)
print("\n5x5 Identity Matrix:\n", identity_arr)

# 4. Array Slicing and Indexing
arr = np.arange(10, 20)
print("\nOriginal Array:", arr)
print("First 5 elements:", arr[:5])
print("Last 3 elements:", arr[-3:])
print("Even numbers:", arr[arr % 2 == 0])

# 5. Random Number Generation
rand_arr = np.random.randint(10, 50, size=(2, 5))
print("\nRandom 2x5 Array:\n", rand_arr)
print("Maximum:", np.max(rand_arr))
print("Minimum:", np.min(rand_arr))
print("Mean:", np.mean(rand_arr))

# 6. Reshape an Array
arr3 = np.arange(1, 13).reshape(3, 4)
print("\n3x4 Matrix:\n", arr3)
print("Transposed Matrix:\n", arr3.T)

# 7. Mathematical Operations
a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])
print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 8. Conditional Selection
arr4 = np.array([5, 10, 15, 20, 25, 30])
greater_than_15 = arr4[arr4 > 15]
print("\nElements greater than 15:", greater_than_15)

# 9. Statistics on Array
arr5 = np.random.rand(10)
print("\nRandom Array:", arr5)
print("Mean:", np.mean(arr5))
print("Median:", np.median(arr5))
print("Standard Deviation:", np.std(arr5))

# 10. Concatenate and Stack Arrays
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
h_concat = np.hstack((x, y))
v_concat = np.vstack((x, y))
print("\nHorizontal Concatenation:\n", h_concat)
print("Vertical Concatenation:\n", v_concat)
