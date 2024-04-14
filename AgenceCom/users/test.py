# Import the User class
from user import User

# Import the UserDao class
from user_dao import UserDao

# Initialize the connection to the database
UserDao.connexion = UserDao.connexion_db()
UserDao.cursor = UserDao.connexion.cursor()

# Get all users from the database
def get_all_users():
    # Call the list_all method of the UserDao class
    return UserDao.list_all()

# Add a user to the database
def add_user(full_name, username, password):
    # Create a User object with the given parameters
    user = User(full_name, username, password)
    # Call the create method of the UserDao class
    return UserDao.create(user)

# Get a user from the database by username and password
def get_user_by_username_password(username, password):
    # Call the get_one method of the UserDao class
    return UserDao.get_one(username, password)

# Example usage
# Import the functions from the __init__.py file
# from. import get_all_users, add_user, get_user_by_username_password

# Get all users from the database
# users = get_all_users()

# Add a user to the database
add_user("Tom Riddle", "voldemort", "horcrux")

# Get a user from the database by username and password
# (message, user) = get_user_by_username_password("voldemort", "horcrux")
# print((message, user))