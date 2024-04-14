import database as db
from users.user import User
import flask_bcrypt as bcrypt

class UserDao:
    # Establish a connection to the database and create a cursor
    connexion = db.connexion_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, utl:User):
        """
        Insert a new user into the 'users' table.
        :param utl: User object containing user information
        :return: A message indicating success or failure
        """
        sql = "INSERT INTO users (full_name, username, password) VALUES (%s, %s, %s)"  # SQL query to insert a new user
        params = (utl.full_name, utl.username, utl.password)  # Parameters for the SQL query
        try:
            UserDao.cursor.execute(sql,params)  # Execute the SQL query
            UserDao.connexion.commit()  # Commit the changes to the database
            message = "Success"  # Set the message to 'Success'
        except Exception as exc:
            message = "Error"  # Set the message to 'Error'
        return message  # Return the message

    @classmethod
    def list_all(cls):
        """
        Retrieve all users from the 'users' table.
        :return: A list of tuples representing users
        """
        sql = "SELECT * FROM users"  # SQL query to select all users
        UserDao.cursor.execute(sql)  # Execute the SQL query
        users = UserDao.cursor.fetchall()  # Fetch all the results
        return users  # Return the results

    @classmethod
    def get_one(cls,username,password):
        """
        Retrieve a specific user from the 'users' table based on username and password.
        :param username: The username of the user
        :param password: The password of the user
        :return: A tuple containing a message and the user if found, or an empty list if not found
        """
        sql = "SELECT * FROM users WHERE username=%s"  # SQL query to select a specific user by username

        try:
            UserDao.cursor.execute(sql, (username,))  # Execute the SQL query with the given username
            user = UserDao.cursor.fetchone()  # Fetch the first result
            if user and bcrypt.check_password_hash(user[3], password):  # Check if the user exists and password matches
                message = "Success"  # Set the message to 'Success'
            else:
                message = "Error"  # Set the message to 'Error'
                user = []  # Set the user to an empty list
        except Exception as ex:
            message = "Error"  # Set the message to 'Error'
            user = []  # Set the user to an empty list

        return message, user  # Return the message and the user