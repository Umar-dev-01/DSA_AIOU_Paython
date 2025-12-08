
"""Lab Task: Pandas Data Handling

Dataset Recommendation (from Kaggle)
Dataset Name: International Student Performance Dataset
(Contains student details, math, reading, writing scores)
Example source name will: Students Performance in Exams
 File Format
The dataset usually comes as a .csv file.
 Your Tass"""


"""Task 1: Load the Dataset
Use Pandas to read the CSV file and display:
First 10 rows
Last 10 rows
File information (using .info())"""
import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")
print(df.head(10))
print(df.tail(10))
print(df.info())



"""Task 2: Basic Analysis
Perform the following:
Show total number of columns and rows
List all column names
Find missing values in the dataset (using .isnull().sum())"""
print(df.shape)
print(df.columns)
print(df.isnull().sum())




"""Task 3: Statistical Operations
Using Pandas:
Calculate the average math score
Calculate the maximum reading score
Calculate the minimum writing score"""
print("Average Math Score:",
 df["math score"].mean())
print("Max Reading Score:",
 df["reading score"].max())
print("Min Writing Score:", 
df["writing score"].min())



"""Task 4: Sorting
Sort data in descending order based on:
Math score
Writing score
(Show results separately)"""
math_sorted = df.sort_values(by="math score", ascending=False)
print(math_sorted)
writing_sorted = df.sort_values(by="writing score", ascending=False)
print(writing_sorted)



"""Task 5: Filterg
Filter and display:
Students who scored more than 80 in math
Students with A-level scores (above 90) in writing"""
math_above_80 = df[df["math score"] > 80]
print(math_above_80)
writing_above_90 = df[df["writing score"] > 90]
print(writing_above_90)



"""Task 6: Save New File
Save the filtered data into a new file named:
high_performers.csv
Create a new column called "Average Score" using:
Average Score = (math + reading + writing) / 3
Then sort by “Average Score” (highest first)."""
df["Average Score"] = (df["math score"] + df["reading score"] + df["writing score"]) / 3
sorted_avg = df.sort_values(by="Average Score", ascending=False)
high_performers = sorted_avg[sorted_avg["Average Score"] > 85]
high_performers.to_csv("high_performers.csv", index=False)
