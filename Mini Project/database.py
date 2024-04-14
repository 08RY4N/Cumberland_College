import mysql.connector

try:
  connexion = mysql.connector.connect(
    host='localhost', # Your MySQL host
    user='root', # Your MySQL username
    password='Bingo12345', # Your MySQL password
    database='my_database' # The name of your MySQL database
  )
  print("Successfully connected to the database.")
except mysql.connector.Error as e:
  print(f"Failed to connect to the database: {e}")