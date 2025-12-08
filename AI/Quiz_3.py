"""Q1. (List / Tuple Concept)

What is the difference between a list and a tuple in Python?
Also write one example of a list and one example of a tuple."""
List:
1. in the list cam cahnge and remove the data
2. List written with []
Example:
my_list = [1, 2, 3]  
Tuple:
1. cam not be change after creation
2. Written with ()
Example:
my_tuple = (1, 2, 3)




"""Q2. (Dictionary Task)
Create a dictionary named student with keys "name", "age", and "marks".
Add this data:
name: Ali
age: 20
marks: 85
Then print only the marks."""

student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}
print(student["marks"])





"""Q3. (NumPy Conversion)
Convert the following list into a NumPy array:
numbers = [10, 20, 30, 40]
After converting, print the array and its type (dtype).""""
import numpy as np
numbers = [10, 20, 30, 40]
arr = np.array(numbers)
print(arr)
print(arr.dtype)


"""Q4. (Pandas CSV Task)
Write Python code using Pandas to create the following data as a DataFrame, then save it into a CSV file named students.csv.
Name Age Grade
Sara 18 A
Hamza 19 B
Ayesha 20 A"""
import pandas as pd
data = {
    "Name": ["Sara", "Hamza", "Ayesha"],
    "Age": [18, 19, 20],
    "Grade": ["A", "B", "A"]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)



""""
Q5. (Array Operation NumPy)
Create a NumPy array:
arr = [2, 4, 6, 8]
Then multiply the array by 3 and print the result."""
import numpy as np
arr = np.array([2, 4, 6, 8])
result = arr * 3
print(result)
