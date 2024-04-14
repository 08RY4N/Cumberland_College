import database as db
from employees.employee import Employee

class EmployeeDao:
    # Initialize the connection to the database
    connexion = db.connexion_db()
    cursor = connexion.cursor()

    # Get all employees from the database
    @classmethod
    def get_all(cls):
        # SQL query to select all employees
        sql = "SELECT * FROM employee"
        # Execute the SQL query
        EmployeeDao.cursor.execute(sql)
        # Fetch all rows from the query
        employers = EmployeeDao.cursor.fetchall()
        return employers

    # Add an employee to the database
    @classmethod
    def add(cls, emp: Employee):
        # SQL query to insert an employee into the database
        sql = "INSERT INTO employee (nom, prenom, badge_number, position, departement) VALUES (%s,%s,%s,%s,%s)"
        # Parameters for the SQL query
        params = (emp.last_name, emp.first_name, emp.badge_number, emp.position, emp.department)
        try:
            # Execute the SQL query with the parameters
            EmployeeDao.cursor.execute(sql, params)
            # Commit the changes to the database
            EmployeeDao.connexion.commit()
            # Set the message to indicate success
            message = "Success"
        except Exception as ex:
            # Set the message to indicate an error
            message = "Error"
        # Return the message
        return message

    # Get an employee from the database by badge number
    @classmethod
    def get_one(cls, badge_number):
        # SQL query to select an employee from the database by badge number
        sql = "SELECT * FROM employee WHERE badge_number=%s"
        try:
            # Execute the SQL query with the badge number
            EmployeeDao.cursor.execute(sql, (badge_number,))
            # Set the message to indicate success
            message = "Success"
            # Fetch the first row from the query
            employe = EmployeeDao.cursor.fetchone()
        except Exception as ex:
            # Set the message to indicate an error
            message = "Error"
            # Set the employee to an empty list
            employe = []
        # Return the message and the employee
        return (message, employe)