**Assignment: Python Data Structures and List Operations**

**1. Queue Implementation**

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        if not self.items:
            print("Queue is empty")
        else:
            removed = self.items.pop(0)
            print(f"Dequeued: {removed}")

    def display(self):
        print("Queue:", self.items)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
```

**2. Stack Implementation Using List**

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if not self.items:
            print("Stack is empty")
        else:
            removed = self.items.pop()
            print(f"Popped: {removed}")

    def display(self):
        print("Stack:", self.items)

# Example usage
s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.display()
s.pop()
s.display()
```

**3. Frequency of Elements Using Dictionary**

```python
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency:", freq)
```

**4. Find Maximum and Minimum Without Built-in Functions**

```python
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Maximum:", max_num)
print("Minimum:", min_num)
```

**5. Reverse a List Without reverse() or Slicing**

```python
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)
```

---

This is written simply and clearly so it looks like your original work.

I can also **combine this with your Bubble Sort assignment into a single Word document** ready to submit. Do you want me to do that?
