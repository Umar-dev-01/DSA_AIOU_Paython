#1: Write a Python program to print your favorite color on the screen.
print("My favorite color is Blue.")



#2: Take user input to create variables of different data types (string, integer, float, and boolean) and display each variable and its type on the screen.
name = input("Enter your name: ")             # string
age = int(input("Enter your age: "))          # integer
height = float(input("Enter your height: "))  # float
is_student = input("Are you a student? (yes/no): ") == "yes"  # boolean

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))



'''33: Ask the user to enter their name and then display a welcome message like: 
Welcome, Ali!'''
name = input("Enter your name: ")
print("Welcome,", name + "!")



#4: Take three numbers as input from the user and print their total sum.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

total = num1 + num2 + num3
print("The total sum is:", total)



#5: Write a Python program to input two numbers and print their average. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2) / 2
print("The average is:", average)



#6: Create 4 variables: a string, an integer, a float, and a boolean.
name = "Umar"
age = 20
height = 5.9
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print("Variables created successfully!")



#7: Print each variable and its data type using the type() function.
name = "Umar"
age = 20
height = 5.9
is_student = True

print(name, "is of type:", type(name))
print(age, "is of type:", type(age))
print(height, "is of type:", type(height))
print(is_student, "is of type:", type(is_student))




#8: Take length and width as user input and calculate the area of a rectangle.
width = float(input("Enter width: "))

area = length * width
print("The area of the rectangle is:", area)




# 9: Write a Python program to convert temperature from Celsius to Fahrenheit.
length = float(input("Enter length: "))
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)




#10: Input principal, rate, and time and calculate simple interest.
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)




#11: Ask the user to input their first name and last name. Combine them into one string and display the full name.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name
print("Your full name is:", full_name)






#12: Take a number as input from the user and print its square.
num = float(input("Enter a number: "))
square = num ** 2
print("The square of the number is:", square)