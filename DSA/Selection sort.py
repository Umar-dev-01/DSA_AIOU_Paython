# Q1 — Selection Sort (Ascending)
arr = [5, 2, 9, 1, 3]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Q1:", arr)


# Q2 — Selection Sort (Descending)
arr = [3, 8, 1, 6, 2]
for i in range(len(arr)):
    max_index = i
    for j in range(i+1, len(arr)):
        if arr[j] > arr[max_index]:
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]
print("Q2:", arr)


# Q3 — Print min index in each pass
arr = [5, 2, 9, 1, 3]
print("Q3:")
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    print("Pass", i+1, "→ min index =", min_index)
    arr[i], arr[min_index] = arr[min_index], arr[i]


# Q4 — Count swaps
arr = [5, 1, 4, 2, 8]
swaps = 0
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1
print("Q4 Sorted:", arr)
print("Total swaps:", swaps)


# Q5 — Float selection sort
arr = [4.2, 1.1, 3.5, 2.7]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Q5:", arr)


# Q6 — Character sorting
arr = ['d', 'a', 'c', 'b']
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Q6:", arr)


# Q7 — kth smallest element
arr = [7, 10, 4, 3, 20, 15]
k = 3
for i in range(k):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Q7 kth smallest:", arr[k-1])


# Q8 — Sort only specific range (2 to 7)
arr = [9, 5, 8, 1, 4, 7, 3, 2, 6]
start = 2
end = 7
for i in range(start, end+1):
    min_index = i
    for j in range(i+1, end+1):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Q8:", arr)


# Q9 — Count elements already in correct sorted position
arr = [5, 1, 4, 2, 8, 3]
sorted_arr = sorted(arr)
count = 0
for i in range(len(arr)):
    if arr[i] == sorted_arr[i]:
        count += 1
print("Q9 correct positions:", count)


# Q10 — Compare comparisons
N = 5
bubble = 0
for i in range(N):
    for j in range(N - i - 1):
        bubble += 1
selection = N * (N - 1) // 2
print("Q10 Bubble comparisons:", bubble)
print("Selection comparisons:", selection)
