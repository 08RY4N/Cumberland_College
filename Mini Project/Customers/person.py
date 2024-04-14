class Person:
    # The Person class represents a person with a name and age.
    def __init__(self, name, age):
        # Initialize private person attributes
        self.__name = name
        self.__age = age

    def get_name(self):
        # Return the person's name.
        return self.__name

    def set_name(self, name):
        # Set the person's name.
        self.__name = name

    def get_age(self):
        # Return the person's age.
        return self.__age

    def set_age(self, age):
        # Set the person's age.
        self.__age = age
