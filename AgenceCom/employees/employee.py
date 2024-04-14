class Employee:
    # Initialize the Employee object with the given parameters
    def __init__(self, last_name, first_name, badge_number, position, department):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__badge_number = badge_number
        self.__position = position
        self.__department = department

    # Get the last name of the employee
    @property
    def last_name(self):
        return self.__last_name

    # Set the last name of the employee
    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    # Get the first name of the employee
    @property
    def first_name(self):
        return self.__first_name

    # Set the first name of the employee
    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    # Get the badge number of the employee
    @property
    def badge_number(self):
        return self.__badge_number

    # Set the badge number of the employee
    @badge_number.setter
    def badge_number(self, value):
        self.__badge_number = value

    # Get the position of the employee
    @property
    def position(self):
        return self.__position

    # Set the position of the employee
    @position.setter
    def position(self, value):
        self.__position = value

    # Get the department of the employee
    @property
    def department(self):
        return self.__department

    # Set the department of the employee
    @department.setter
    def department(self, value):
        self.__department = value