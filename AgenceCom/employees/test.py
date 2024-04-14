# Import the EmployeeDao class
from employee_dao import EmployeeDao

# Initialize the connection to the database
EmployeeDao.connexion = EmployeeDao.connexion_db()
EmployeeDao.cursor = EmployeeDao.connexion.cursor()

# Get all employees from the database
def get_all_employees():
    # Call the get_all method of the EmployeeDao class
    return EmployeeDao.get_all()

# Add an employee to the database
def add_employee(last_name, first_name, badge_number, position, department):
    # Create an Employee object with the given parameters
    emp = Employee(last_name, first_name, badge_number, position, department)
    # Call the add method of the EmployeeDao class
    return EmployeeDao.add(emp)

# Get an employee from the database by badge number
def get_employee_by_badge_number(badge_number):
    # Call the get_one method of the EmployeeDao class
    return EmployeeDao.get_one(badge_number)

# Example usage
# Import the functions from the __init__.py file
# from. import get_all_employees, add_employee, get_employee_by_badge_number

# Get all employees from the database
# employees = get_all_employees()

# Add an employee to the database
# add_employee("Dobby", "", "DOBY1234", "House-elf", "Kitchen")

# Get an employee from the database by badge number
# (message, employee) = get_employee_by_badge_number("HP1234")
# print((message, employee))
