import database

class CinemaRoom:
    def __init__(self):
        # Establish connection to the database
        self.connection = database.connect_to_database()
        self.cursor = self.connection.cursor()

    def reserve_seat(self, name, seat):
        # Reserve a seat for a person and save it to the database
        sql = "INSERT INTO Reservations (name, seat) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, seat))
        self.connection.commit()
        print(f"Seat {seat} has been reserved for {name}.")

    def show_reserved_seats(self):
        # Show reserved seats by retrieving data from the database
        sql = "SELECT * FROM Reservations"
        self.cursor.execute(sql)
        reservations = self.cursor.fetchall()
        print("Reserved seats:")
        for reservation in reservations:
            print(f"{reservation[0]} has reserved seat {reservation[1]}.")

    def filter_reservations_by_person(self, name):
        # Filter reservations by person and display them
        sql = "SELECT * FROM Reservations WHERE name = %s"
        self.cursor.execute(sql, (name,))
        reservations = self.cursor.fetchall()
        if reservations:
            print(f"Reservations for {name}:")
            for reservation in reservations:
                print(f"{reservation[0]} has reserved seat {reservation[1]}.")
        else:
            print(f"No reservations found for {name}.")

    def cancel_reservation(self, name):
        # Cancel all reservations made by a specific person
        sql = "DELETE FROM Reservations WHERE name = %s"
        self.cursor.execute(sql, (name,))
        self.connection.commit()
        print(f"All reservations for {name} have been canceled.")

    def reserve_special_seat(self, name):
        # Reserve a special seat for a disabled person and save it to the database
        # Example: seat 100 is reserved for disabled persons
        sql = "INSERT INTO Reservations (name, seat) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, 100))
        self.connection.commit()
        print(f"A special seat has been reserved for {name}.")

    def __del__(self):
        # Close cursor and connection to the database
        self.cursor.close()
        self.connection.close()