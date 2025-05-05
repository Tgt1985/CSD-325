# Sean Dudley
# CSD325 - Module 8 Assignment - JSON
# 5/4/2025

import json



def print_student(students):

    for student in students:
        print(f"{student['L_Name']},{student['F_Name']} : Student_ID - {student['Student_ID']}, Email - {student['Email']}")

# Load the JSON file
with open (rf'C:\Users\seanm\OneDrive\Desktop\School Copies\Bellevue\2025\Needed Files\student.json', 'r') as file:
    students = json.load(file)        

# Display provided list, before adding new student

print('____________________Provided Student List____________________')
print()
print_student(students)
print()    

# Append students with new_student

new_student = {

    "F_Name": "Sean",
    "L_Name": "Dudley",
    "Student_ID": "120558",
    "Email": "sean.dudley@my365.belleve.edu"

}
students.append(new_student)

# Display current student list, after adding known new student(s)

print('____________________Current Student List____________________')
print()
print_student(students)
print()

# Confirm before saving changes

print('Your file has been updated.')

    # Save Current student list back to json file
with open(rf'C:\Users\seanm\OneDrive\Desktop\School Copies\Bellevue\2025\Needed Files\student.json', 'w') as file:
    json.dump(students, file)

print('The student.json files has been updated with the new student information. ')