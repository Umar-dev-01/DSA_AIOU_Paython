# Q1: Bubble Sort (Ascending Order)
# Simple program to sort 5 numbers using bubble sort

nums = [5, 2, 9, 1, 3]
n = len(nums)

for i in range(n - 1):
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted array:", nums)



# Q2: Bubble Sort in Descending Order
# Just change the sign to sort from largest to smallest

arr = [3, 8, 1, 6, 2]
n = len(arr)

for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted in descending order:", arr)



# Q3: Bubble Sort with Swap Counter
# Count how many swaps happen in total

nums = [5, 1, 4, 2, 8]
count_swaps = 0
n = len(nums)

for i in range(n - 1):
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            count_swaps += 1

print("Sorted array:", nums)
print("Total swaps:", count_swaps)



# Q4: Optimized Bubble Sort
# Stop early if no swaps happen (already sorted)

numbers = [1, 2, 3, 4, 5]
n = len(numbers)
passes = 0

for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
    passes += 1
    if not swapped:
        break

print("Array sorted in", passes, "pass(es)")
print("Sorted array:", numbers)



# Q5: Bubble Sort for Floating Point Numbers
# Works same way as integers

floats = [4.2, 1.1, 3.5, 2.7]
n = len(floats)

for i in range(n - 1):
    for j in range(n - i - 1):
        if floats[j] > floats[j + 1]:
            floats[j], floats[j + 1] = floats[j + 1], floats[j]

print("Sorted floating numbers:", floats)



# Q6: Bubble Sort for Characters
# Sorts alphabets alphabetically

letters = ['d', 'a', 'c', 'b']
n = len(letters)

for i in range(n - 1):
    for j in range(n - i - 1):
        if letters[j] > letters[j + 1]:
            letters[j], letters[j + 1] = letters[j + 1], letters[j]

print("Sorted characters:", letters)



# Q7: Bubble Sort on a Specific Range
# Sort only between given indexes

data = [9, 3, 8, 1, 4, 7, 2]
start = 2
end = 6
length = end - start + 1

for i in range(length - 1):
    for j in range(start, end - i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("Array after sorting range:", data)
