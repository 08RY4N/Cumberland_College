from Customers.person import Person  # Importing the Person class from the person module
from Customers.person_dao import PersonList  # Importing the PersonList class from the person_dao module
from WaitingList.queue import Queue  # Importing the Queue class from the queue module
from Rooms.cinemaRoom import CinemaRoom  # Importing the CinemaRoom class from the cinemaRoom module

def display_main_menu():  # Function to display the main menu
    print("\nMain Menu:")
    print("1. Manage Persons")
    print("2. Manage Queue")
    print("3. Manage Cinema Room")
    print("0. Quit")

def display_person_menu():  # Function to display the person menu
    print("\nManage Persons:")
    print("1. Add Person")
    print("2. Show All Persons")
    print("3. Filter Persons by Age")
    print("4. Search Person by Name")
    print("0. Back to Main Menu")

def display_queue_menu():  # Function to display the queue menu
    print("\nManage Queue:")
    print("1. Add Person to Queue")
    print("2. Remove Person from Queue")
    print("3. Add Priority Person to Queue")
    print("0. Back to Main Menu")

def display_cinema_room_menu():  # Function to display the cinema room menu
    print("\nManage Cinema Room:")
    print("1. Reserve Seat")
    print("2. Show Reserved Seats")
    print("3. Filter Reservations by Person")
    print("4. Cancel Reservations for Person")
    print("5. Reserve Special Seat")
    print("0. Back to Main Menu")

def manage_persons(persons):  # Function to manage persons
    while True:
        display_person_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter the person's name: ")
            age = int(input("Enter the person's age: "))
            person = Person(name, age)
            persons.add_person(person)
        elif choice == "2":
            persons.show_persons()
        elif choice == "3":
            min_age = int(input("Enter the minimum age: "))
            max_age = int(input("Enter the maximum age: "))
            persons.filter_persons_by_age(min_age, max_age)
        elif choice == "4":
            name = input("Enter the name of the person to search: ")
            persons.search_person(name)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def manage_queue(queue):  # Function to manage the queue
    while True:
        display_queue_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter the name of the person to add to the queue: ")
            queue.add_person_to_queue(name)
        elif choice == "2":
            queue.remove_person_from_queue()
        elif choice == "3":
            name = input("Enter the name of the priority person to add to the queue: ")
            queue.add_priority_person_to_queue(name)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def manage_cinema_room(cinema_room):  # Function to manage the cinema room
    while True:
        display_cinema_room_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter the name of the person reserving the seat: ")
            seat = int(input("Enter the seat number to reserve: "))
            cinema_room.reserve_seat(name, seat)
        elif choice == "2":
            cinema_room.show_reserved_seats()
        elif choice == "3":
            name = input("Enter the name of the person to filter reservations: ")
            cinema_room.filter_reservations_by_person(name)
        elif choice == "4":
            name = input("Enter the name of the person to cancel reservations: ")
            cinema_room.cancel_reservation(name)
        elif choice == "5":
            name = input("Enter the name of the person to reserve special seat: ")
            cinema_room.reserve_special_seat(name)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def main():  # Main function
    persons = PersonList()
    queue = Queue()
    cinema_room = CinemaRoom()

    while True:
        display_main_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            manage_persons(persons)
        elif choice == "2":
            manage_queue(queue)
        elif choice == "3":
            manage_cinema_room(cinema_room)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
