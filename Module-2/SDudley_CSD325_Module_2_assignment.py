






# Create a constant for a loop
another = 'y'

# Create the base class (Student)
class Student:
    # Initialize the Student class
    def __init__(self, UI_stu_first_name, UI_stu_last_name, UI_stu_grade, stu_credits):
        self.stu_first_name = UI_stu_first_name
        self.stu_last_name = UI_stu_last_name
        self.stu_grade = UI_stu_grade
        self.grade_point = 0
        self.grade_points = 0
        self.stu_credits = 0
        self.stu_GPA = 0

    # Create a method to calculate the student's GPA
    def calculateGPA(self, stu_grade, UI_stu_credits):
        self.stu_credits = int(self.stu_credits) + UI_stu_credits
        if stu_grade == 'A':
            self.grade_point = (int(self.grade_point) + (UI_stu_credits * 4.0))
        if stu_grade == 'B+':
            self.grade_point = (int(self.grade_point) + (UI_stu_credits * 3.5))
        if stu_grade == 'B':
            self.grade_point = (int(self.grade_point) + (UI_stu_credits * 3.0))
        if stu_grade == 'C+':
            self.grade_point = (int(self.grade_point) + (UI_stu_credits * 2.5))
        if stu_grade == 'C':
            self.grade_point = (int(self.grade_point) + (UI_stu_credits * 2.0))
        if stu_grade == 'D':
            self.grade_point = (int(self.grade_point) + (UI_stu_credits * 1.0))            
        else:
            self.grade_point = (int(self.grade_point) + (UI_stu_credits * 0.0))

        self.stu_GPA = ((self.grade_point) / int(UI_stu_credits))

    # Create a method to retrieve the student's GPA
    def getGPA(self):
        print(f'The GPA for {self.stu_first_name} {self.stu_last_name} is {round(self.stu_GPA, 1)}')


# Create subclass for a declared student
class Declared_Student(Student):
    def __init__(self, UI_stu_first_name, UI_stu_last_name, UI_stu_concentration, UI_stu_grade, UI_stu_credits):
        super(Student, self).__init__()
        self.stu_first_name = UI_stu_first_name
        self.stu_last_name = UI_stu_last_name
        self.concentration = UI_stu_concentration        
        self.stu_grade = UI_stu_grade
        self.grade_point = 0
        self.stu_credits = UI_stu_credits
        
    
    # Create a method to retrieve the student's study concentration
    def getConcentration(self):
        return self.concentration
    
    # Create a method to calculate what year of studies the student is in 
    def getYear(self):

        if self.concentration == 'NA':
            return f"{self.stu_first_name} {self.stu_last_name} has not selected a concentration."
        if self.stu_credits <= 33:
            return f"{self.stu_first_name} {self.stu_last_name} is a Year One Student in {UI_stu_concentration}."
        if self.stu_credits <= 66:
            return f"{self.stu_first_name} {self.stu_last_name} is a Year Two Student in {UI_stu_concentration}."
        if self.stu_credits <= 96:
            return f"{self.stu_first_name} {self.stu_last_name} is a Year Three Student in {UI_stu_concentration}."
        if self.stu_credits < 130:
            return f"{self.stu_first_name} {self.stu_last_name} is a Year Four Student in {UI_stu_concentration}."
        else:
            return f"{self.stu_first_name} {self.stu_last_name} is a Multiyear Student in {UI_stu_concentration}." 
        

# User input values for name, as this will not be asked for every grade/credit entry
# UI_stu_concentration could be added to the while loop, if we were adding to a dictionary to make sure the student
# did not change concentrations or begin a new concentration once graduated.

UI_stu_first_name = input("Please enter the student's first name: ")
UI_stu_last_name = input("Please enter the student's last name: ")
UI_stu_concentration = input('Please enter the student concentration area. If the student is undeclared, please enter in NA: ').upper()

while another == 'y':

    # User input values, these will be asked for every new entry added for each user
    UI_stu_grade = input("Please enter the student's grade: ").upper()
    UI_stu_credits = int(input("Please enter the credits: "))

    # Ask the user if they would like to enter more infomration about that student
    another = input(f'Would you like to enter more information for {UI_stu_first_name} {UI_stu_last_name}? (y or n)')   

else:
    pass    
                    
# Create a student object
    student_info = Student(UI_stu_first_name, UI_stu_last_name, UI_stu_grade, UI_stu_credits)


# Create a Declared_Student object
student_info = Declared_Student(UI_stu_first_name, UI_stu_last_name,UI_stu_concentration, UI_stu_grade, UI_stu_credits)


# Using the student object, calculate and display the student's GPA
student_info.calculateGPA(UI_stu_grade, UI_stu_credits)

# Use the student object to run the getGPA method
student_info.getGPA()

# Use the student object to run the getYear method
student_year = student_info.getYear()

# As a print function was not used at the end of the getYear method, print the student_year
print(student_year)