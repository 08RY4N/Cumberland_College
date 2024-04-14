# Importing the mysql.connector module
import mysql.connector as mysql

# Defining a function to connect to the database
def connexion_db():

    # Returning a connection object to the 'agence' database
    return mysql.connect(
        # The username for the database connection
        user='root',
        # The password for the database connection
        password='Bingo12345',
        # The host where the database is located
        host='localhost',
        # The name of the database to connect to
        database='agence'
        )