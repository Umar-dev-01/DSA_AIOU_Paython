**Assignment: Flow Control and Loops in Python**

**Flow Control (if-else) Questions**

**1. Even or Odd**

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**2. Positive, Negative, or Zero**

```python
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

**3. Largest of Three Numbers**

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest is", a)
elif b >= a and b >= c:
    print("Largest is", b)
else:
    print("Largest is", c)
```

**4. Leap Year Checker**

```python
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

**5. Vowel or Consonant**

```python
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print("Vowel")
else:
    print("Consonant")
```

**6. Pass or Fail**

```python
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

**7. Eligible to Vote or Not**

```python
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

**8. Odd/Even Sum Checker**

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum_ab = a + b
if sum_ab % 2 == 0:
    print("Sum is Even")
else:
    print("Sum is Odd")
```

---

**Loop Questions**

**Using for Loop**

**1. Print 1 to 10**

```python
for i in range(1, 11):
    print(i, end=' ')
```

**2. Sum of N Natural Numbers**

```python
n = int(input("Enter n: "))
total = 0
for i in range(1, n+1):
    total += i
print("Sum:", total)
```

**3. Multiplication Table**

```python
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
```

**4. Factorial of a Number**

```python
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)
```

**5. Count Even and Odd Numbers**

```python
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
```

---

This is simple, clear, and looks like your own work.

I can also **combine this with your previous Bubble Sort and Data Structure assignments** into a single Word file ready for submission.

Do you want me to do that next?
