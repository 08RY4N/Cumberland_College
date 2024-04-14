import mysql.connector 

# Connect to the MySQL database
connexion = mysql.connector.connect(
  host='localhost', # Your MySQL host
  user='newuser', # Your MySQL username
  password='newpassword', # Your MySQL password
  database='newdatabase' # The name of your MySQL database
)

# Create a new user in the user table
def create_user(name, email):
    cursor = connexion.cursor()
    cursor.execute("""
        INSERT INTO user (name, email)
        VALUES (%s,%s)    
    """, (name, email))
    connexion.commit()

# Read all users from the user table
def read_user():
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM user")
    for (id, name, email) in cursor:
        print(f"\nID: {id}, Name: {name}, Email: {email}")

# Update the email of a user with a given ID
def update_user(id, email):
    cursor = connexion.cursor()
    cursor.execute("UPDATE user SET email=%s WHERE id=%s", (email, id))
    connexion.commit()

# Delete a user with a given ID
def delete_user(id):
    cursor = connexion.cursor()
    cursor.execute("DELETE FROM user WHERE id=%s", (id,))
    connexion.commit()

# Example usage
# create_user("John Wick", "john.wick@high.table")
# read_user()
# update_user(1, "john.wick@low.table")
# delete_user(1)