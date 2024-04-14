class Department:
    # Initialize the Department object with name, location, and head
    def __init__(self,name,location,head):
        self.__name = name  # The name of the department
        self.__location = location  # The location of the department
        self.__head = head  # The head of the department

    # Getter for the name property
    @property
    def name(self):
        return self.__name

    # Setter for the name property
    @name.setter
    def name(self, value):
        self.__name = value

    # Getter for the location property
    @property
    def location(self):
        return self.__location

    # Setter for the location property
    @location.setter
    def location(self, value):
        self.__location = value

    # Getter for the head property
    @property
    def head(self):
        return self.__head

    # Setter for the head property
    @head.setter
    def head(self, value):
        self.__head = value