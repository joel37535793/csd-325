import json

# Load student.json file
with open('student.json', 'r') as file:
    students = json.load(file)


# Function to print students
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")


# ----- Original Student List -----
print("Original Student List")
print_students(students)


# Append new student (change this to YOUR info)
new_student = {
    "F_Name": "Joel",
    "L_Name": "Baby",
    "Student_ID": 21452560,
    "Email": "jbaby@my365.bellevue.edu"
}

students.append(new_student)


# ----- Updated Student List -----
print("\nUpdated Student List")
print_students(students)


# Write data back to JSON file
with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)


print("\nJSON file updated")