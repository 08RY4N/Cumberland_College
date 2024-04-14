import database as db
from departments.department import Department

class DepartmentDao:
    # Initialize the database connection and cursor
    connection = db.connexion_db()
    cursor = connection.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, dpt:Department):
        # SQL query to insert a new department into the database
        sql = "INSERT INTO department (name,location,head) VALUES (%s,%s,%s)"
        # Parameters for the SQL query
        params = (dpt.name, dpt.location, dpt.head)
        try:
            # Execute the SQL query with the parameters
            DepartmentDao.cursor.execute(sql,params)
            # Commit the changes to the database
            DepartmentDao.connection.commit()
            # Return a success message
            message = "Success"
        except Exception as exc:
            # Return an error message if there was an exception
            message = "Error"
        return message
    
    @classmethod
    def list_all(cls):
        # SQL query to select all departments from the database
        sql = "SELECT * FROM department"
        # Execute the SQL query
        DepartmentDao.cursor.execute(sql)
        # Fetch all the rows returned by the query
        Departments = DepartmentDao.cursor.fetchall()
        
        return Departments
    
    @classmethod
    def delete(cls,id):
        # SQL query to delete a department from the database
        sql = "DELETE FROM department WHERE id=%s"
        # Execute the SQL query with the department id
        DepartmentDao.cursor.execute(sql,(id,))
        # Commit the changes to the database
        DepartmentDao.connection.commit()
        
        print(f"Deletion of department with id : {id}.")

    @classmethod
    def update(cls,id, dpt:Department):
        # SQL query to update a department in the database
        sql = "UPDATE department SET name=%s,location=%s WHERE id=%s"
        # Parameters for the SQL query
        params = (id,dpt.name, dpt.location)
        # Execute the SQL query with the parameters
        DepartmentDao.cursor.execute(sql,params)
        # Commit the changes to the database
        DepartmentDao.connection.commit()
        
        print(f"Update of department : {dpt.name}.")