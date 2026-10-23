
import pandas as pd
import numpy as np

class Student:
    def __init__(self, name, average):
        self.name = name
        self.average = average
    def calculate_grade(self):
        if self.average >= 90:
            return "A+"
        elif self.average >= 80:
            return "A"
        elif self.average >= 70:
            return "B"
        elif self.average >= 60:
            return "C"
        else:
            return "F"
    def check_result(self):
        if self.average >= 40:
            return "Pass"
        else:
            return "Fail"

def calculate_total(*marks):
    return sum(marks)

df = pd.read_csv("students.csv")

subjects = ("Python", "Java", "SQL")
totals = []
averages = []
grades = []
results = []

for index, row in df.iterrows():
    marks = [row["Python"], row["Java"], row["SQL"]]
    total = calculate_total(*marks)
    average = total / len(subjects)
    student = Student(row["Name"], average)
    totals.append(total)
    averages.append(average)
    grades.append(student.calculate_grade())
    results.append(student.check_result())

df["Total"] = totals
df["Average"] = averages
df["Grade"] = grades
df["Result"] = results

highest = np.max(df["Total"])
lowest = np.min(df["Total"])
class_average = np.mean(df["Average"])
highest_student = df[df["Total"] == highest]
lowest_student = df[df["Total"] == lowest]

top_students = df[df["Total"] == highest]

python_average = np.mean(df["Python"])
java_average = np.mean(df["Java"])
sql_average = np.mean(df["SQL"])

print("=" * 100)
print("                      STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 100)
print("\n============================ STUDENT DATA ============================")
print(df[[
    "Student_ID", "Name", "Department",
    "Python", "Java", "SQL", "Attendance"
]].to_string(index=False))
print("\n============================ STUDENT PERFORMANCE ============================")
print(df[[
    "Student_ID", "Name", "Total",
    "Average", "Grade", "Result"
]].to_string(index=False))
print("\n============================ OVERALL ANALYSIS ============================")
print("Highest Total Marks:", highest)
print("Student(s) with Highest Marks:")
print(highest_student[["Name", "Total"]].to_string(index=False))
print("\nLowest Total Marks:", lowest)
print("Student(s) with Lowest Marks:")
print(lowest_student[["Name", "Total"]].to_string(index=False))
print("Class Average Marks:", round(class_average, 2))
print("\n============================ SUBJECT-WISE ANALYSIS ============================")
print("Python Average:", round(python_average, 2))
print("Java Average:", round(java_average, 2))
print("SQL Average:", round(sql_average, 2))
print("\n============================ TOP-PERFORMING STUDENTS ============================")
print(top_students[["Student_ID", "Name", "Total", "Average", "Grade"]].to_string(index=False))
df.to_csv("student_analysis.csv", index=False)
print("\nAnalysis saved to student_analysis.csv")