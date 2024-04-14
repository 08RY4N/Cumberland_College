import database

class PersonList:
    # The PersonList class represents the list of persons stored in the database.
    def __init__(self):
        # Establish connection to the database
        self.connection = database.connect_to_database()
        self.cursor = self.connection.cursor()

    def add_person(self, person):
        # Insert a new person into the database
        sql = "INSERT INTO Persons (name, age) VALUES (%s, %s)"
        values = (person.get_name(), person.get_age())
        self.cursor.execute(sql, values)
        self.connection.commit()

    def show_persons(self):
        # Retrieve and display all persons from the database
        self.cursor.execute("SELECT * FROM Persons")
        persons = self.cursor.fetchall()
        for person in persons:
            print(person)

    def __del__(self):
        # Close cursor and database connection when the object is deleted
        self.cursor.close()
        self.connection.close()
    
    def search_person(self, name):
        # Search for a person by name in the database
        sql = "SELECT * FROM Persons WHERE name LIKE %s"
        name_pattern = '%' + name + '%'  # Use wildcard to search for partial name
        self.cursor.execute(sql, (name_pattern,))
        found_persons = self.cursor.fetchall()
        if found_persons:
            print("Persons found:")
            for person in found_persons:
                print(person)
        else:
            print("No persons found with the given name.")

    def filter_persons_by_age(self, min_age, max_age):
        # Filter persons by age range in the database
        sql = "SELECT * FROM Persons WHERE age BETWEEN %s AND %s"
        self.cursor.execute(sql, (min_age, max_age))
        filtered_persons = self.cursor.fetchall()
        if filtered_persons:
            print(f"Persons in age range {min_age} to {max_age} :")
            for person in filtered_persons:
                print(person)
        else:
            print("No persons found in the given age range.")