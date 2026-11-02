""" Employee Logging Program 

This program allows an organization to add new employees, generate unique employee ID numbers, and display employee information after all employees have been created. """ 

from random import randrange 

def main(): # Display the purpose of the program print("This program creates a log of new employees and their ID numbers.") 

# Create empty lists 
employees = [] 
employee_ids = [] 
employee_names = [] 
 
# Ask how many employees will be added 
amount = int(input("How many new employees are being added? ")) 
 
# Create each employee 
for number in range(amount): 
    print("\nCreating employee", number + 1) 
    create_employee(employees, employee_ids, employee_names) 
 
# Display the complete employee list 
print("\nEmployee List:") 
print(employees) 
 
# Display each employee's information 
print("\nEmployee Details:") 
for employee in employees: 
    output_employee(employee) 
 
print("\nCompleted by, Brock Harrison") 
  

def create_employee(employees, employee_ids, employee_names): """ Creates a new employee and adds their information to the log. 

Arguments: 
    employees (list): List containing employee dictionaries. 
    employee_ids (list): List containing existing employee IDs. 
    employee_names (list): List containing existing employee names. 
""" 
 
# Ask for employee name 
name = input("Enter employee name: ") 
 
# Check for duplicate names without case sensitivity 
while name.lower() in [existing.lower() for existing in employee_names]: 
    print("This employee already exists. Please enter another name.") 
    name = input("Enter employee name: ") 
 
# Add the new name to the list 
employee_names.append(name) 
 
# Generate a unique employee ID 
employee_id = randrange(1, 501) 
 
while employee_id in employee_ids: 
    employee_id = randrange(1, 501) 
 
# Add the ID to the existing ID list 
employee_ids.append(employee_id) 
 
# Create the employee dictionary 
employee = { 
    "name": name, 
    "ID": employee_id 
} 
 
# Add employee dictionary to the employee list 
employees.append(employee) 
  

def output_employee(employee): """ Displays an employee's name and ID number. 

Arguments: 
    employee (dict): Dictionary containing an employee's name and ID. 
""" 
 
print("Employee created: " + employee["name"]) 
print("Employee ID: " + str(employee["ID"])) 
  

if name == "main": main() 