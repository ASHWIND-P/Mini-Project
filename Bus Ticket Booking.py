class Bus:
    def __init__(self, bus_number, source, destination, total_seats, fare):
        self.bus_number = bus_number
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats  # initially all seats are available
        self.fare = fare

    def book_ticket(self, seats):
        if self.available_seats >= seats:
            self.available_seats -= seats
            print(f"Booking successful! {seats} seats booked on Bus {self.bus_number}.")
        else:
            print(f"Sorry, only {self.available_seats} seats are available on Bus {self.bus_number}.")

    def cancel_ticket(self, seats):
        if self.total_seats - self.available_seats >= seats:
            self.available_seats += seats
            print(f"{seats} seats have been successfully canceled on Bus {self.bus_number}.")
        else:
            print("Error: You can't cancel more seats than were booked.")

    def display_info(self):
        print(f"Bus {self.bus_number}: {self.source} -> {self.destination}")
        print(f"Total Seats: {self.total_seats}, Available Seats: {self.available_seats}")
        print(f"Fare: {self.fare} per seat")


# Function to show available buses
def show_buses(buses):
    print("\nAvailable Buses:")
    for bus in buses:
        bus.display_info()
        print("-" * 30)


# Function to handle booking of tickets
def book_ticket(buses):
    bus_number = int(input("Enter the bus number you want to book tickets for: "))
    found = False
    for bus in buses:
        if bus.bus_number == bus_number:
            found = True
            seats = int(input(f"Enter the number of seats to book (Available seats: {bus.available_seats}): "))
            bus.book_ticket(seats)
            break

    if not found:
        print("Bus number not found. Please try again.")


# Function to handle canceling of tickets
def cancel_ticket(buses):
    bus_number = int(input("Enter the bus number for cancellation: "))
    found = False
    for bus in buses:
        if bus.bus_number == bus_number:
            found = True
            seats = int(input(f"Enter the number of seats to cancel (Booked seats: {bus.total_seats - bus.available_seats}): "))
            bus.cancel_ticket(seats)
            break

    if not found:
        print("Bus number not found. Please try again.")


# Main menu function
def main_menu(buses):
    while True:
        print("\n=== Bus Ticket Booking System ===")
        print("1. Show Available Buses")
        print("2. Book Tickets")
        print("3. Cancel Tickets")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_buses(buses)
        elif choice == "2":
            book_ticket(buses)
        elif choice == "3":
            cancel_ticket(buses)
        elif choice == "4":
            print("Thank you for using the bus booking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Creating bus objects
    bus1 = Bus(101, "New York", "Los Angeles", 50, 100)
    bus2 = Bus(102, "Chicago", "Miami", 40, 90)
    bus3 = Bus(103, "San Francisco", "Seattle", 30, 120)

    # List of buses
    buses = [bus1, bus2, bus3]

    # Calling the main menu function to start the program
    main_menu(buses)
