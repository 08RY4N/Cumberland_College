# Import the Department class
# from department import Department

# Import the DepartmentDao class
from department_dao import DepartmentDao

# Initialize the connection to the database
DepartmentDao.connexion = DepartmentDao.connexion_db()
DepartmentDao.cursor = DepartmentDao.connexion.cursor()

# Get all departments from the database
def get_all_departments():
    # Call the list_all method of the DepartmentDao class
    return DepartmentDao.list_all()

# Add a department to the database
def add_department(name, location, head):
    # Create a Department object with the given parameters
    department = Department(name, location, head)
    # Call the create method of the DepartmentDao class
    return DepartmentDao.create(department)

# Get a department from the database by id
def get_department_by_id(id):
    # Call the get_one method of the DepartmentDao class
    return DepartmentDao.get_one(id)

# Example usage
# Import the functions from the __init__.py file
#from. import get_all_departments, add_department, get_department_by_id

# Get all departments from the database
#departments = get_all_departments()

# Add a department to the database
#add_department("Kitchen", "level 1", "Dobby")

# Get a department from the database by id
#(message, department) = get_department_by_id(1)
#print((message, department))