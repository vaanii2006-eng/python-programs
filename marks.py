import numpy as np

# Marks of 5 students (Rows = Students, Columns = Subjects)
marks = np.array([
    [85, 78, 90],
    [70, 88, 75],
    [60, 65, 70],
    [95, 92, 89],
    [80, 85, 88]
])

print("Marks of Students:\n", marks)

# Total marks of each student
total = np.sum(marks, axis=1)
print("Total Marks of Each Student:", total)

# Average marks of each student
average = np.mean(marks, axis=1)
print("Average Marks of Each Student:", average)

# Highest mark in class
highest = np.max(marks)
print("Highest Mark in Class:", highest)

# Lowest mark in class
lowest = np.min(marks)
print("Lowest Mark in Class:", lowest)

# Class average
class_average = np.mean(marks)
print("Class Average:", class_average)
