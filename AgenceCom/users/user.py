class User:
    # Constructor for User class
    def __init__(self, full_name, username, password):
        # Private instance variables for full_name, username, and password
        self.__full_name = full_name
        self.__username = username
        self.__password = password

    # Getter for full_name
    @property
    def full_name(self):
        return self.__full_name

    # Setter for full_name
    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    # Getter for username
    @property
    def username(self):
        return self.__username

    # Setter for username
    @username.setter
    def username(self, value):
        self.__username = value

    # Getter for password
    @property
    def password(self):
        return self.__password

    # Setter for password
    @password.setter
    def password(self, value):
        self.__password = value