import database

class Queue:
    def __init__(self):
        # Establish connection to the database
        self.connection = database.connect_to_database()
        self.cursor = self.connection.cursor()

    def add_person_to_queue(self, name):
        # Add a person to the queue
        sql = "INSERT INTO Queue (name) VALUES (%s)"
        self.cursor.execute(sql, (name,))
        self.connection.commit()

    def remove_person_from_queue(self):
        # Remove a person from the queue
        # Check if there are any prioritized people in the queue
        self.cursor.execute("SELECT * FROM Queue WHERE priority = 1")
        prioritized_person = self.cursor.fetchone()
        if prioritized_person:
            print(f"Priority person removed from the queue: {prioritized_person[0]}")
            sql = "DELETE FROM Queue WHERE name = %s AND priority = 1"
            self.cursor.execute(sql, (prioritized_person[0],))
            self.connection.commit()
        else:
            # If no prioritized person, remove the first person in the queue
            self.cursor.execute("SELECT * FROM Queue LIMIT 1")
            first_person = self.cursor.fetchone()
            if first_person:
                print(f"Person removed from the queue: {first_person[0]}")
                sql = "DELETE FROM Queue WHERE name = %s"
                self.cursor.execute(sql, (first_person[0],))
                self.connection.commit()
            else:
                print("Queue is empty.")

    def add_priority_person_to_queue(self, name):
        # Add a priority person to the queue
        sql = "INSERT INTO Queue (name, priority) VALUES (%s, 1)"
        self.cursor.execute(sql, (name,))
        self.connection.commit()

    def __del__(self):
        # Close cursor and database connection when the object is deleted
        self.cursor.close()
        self.connection.close()
