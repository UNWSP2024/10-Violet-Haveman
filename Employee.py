# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.
from tkinter.font import names


# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.
class Employee:
    def __init__(self, name, ID_number, department, title):
        self.name = name
        self.ID_number = ID_number
        self.department = department
        self.title = title

    def __str__(self):
        return f"Name: {self.name}, ID: {self.ID_number}, Department: {self.department}, Title: {self.title}"

def employees():
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice president")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    print("First Employee: ", employee1)
    print("Second Employee: ", employee2)
    print("Third Employee: ", employee3)

employees()