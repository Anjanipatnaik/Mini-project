class Event:
    def __init__(self, event_id, name, date, location, cost):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.cost = cost

    def __str__(self):
        return f"Event ID: {self.event_id}\nName: {self.name}\nDate: {self.date}\nLocation: {self.location}\nCost: ₹{self.cost:,.2f}\n"

class EventManagementSystem:
    def __init__(self):
        self.events = []  # List to store events
        self.next_id = 1  # To generate unique event IDs

    def create_event(self):
        print("\nCreate a new event:")
        name = input("Enter event name: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        location = input("Enter event location: ")
        while True:
            try:
                cost = float(input("Enter event cost in Rupees (₹): ₹"))
                if cost < 0:
                    raise ValueError("Cost cannot be negative. Please enter a valid amount.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid positive number for cost.")
        event = Event(self.next_id, name, date, location, cost)
        self.events.append(event)
        print(f"Event '{name}' created successfully!\n")
        self.next_id += 1
    def read_events(self):
        print("\nList of all events:")
        if not self.events:
            print("No events available.")
        else:
            for event in self.events:
                print(event)

    def update_event(self):
        event_id = int(input("\nEnter the event ID to update: "))
        event = self.find_event_by_id(event_id)

        if event:
            print("\nCurrent event details:")
            print(event)

            name = input("Enter new event name (leave blank to keep current): ")
            date = input("Enter new event date (leave blank to keep current): ")
            location = input("Enter new event location (leave blank to keep current): ")
            while True:
                try:
                    cost_input = input("Enter new event cost (leave blank to keep current): ₹")
                    if cost_input:
                        cost = float(cost_input)
                        if cost < 0:
                            raise ValueError("Cost cannot be negative. Please enter a valid amount.")
                        event.cost = cost
                    break
                except ValueError as e:
                    if cost_input == "":  
                        break
                    print(f"Invalid input: {e}. Please enter a valid positive number for cost.")

            
            if name:
                event.name = name
            if date:
                event.date = date
            if location:
                event.location = location

            print(f"Event '{event.name}' updated successfully!\n")
        else:
            print("Event not found!")

    def delete_event(self):
        event_id = int(input("\nEnter the event ID to delete: "))
        event = self.find_event_by_id(event_id)

        if event:
            self.events.remove(event)
            print(f"Event '{event.name}' deleted successfully!\n")
        else:
            print("Event not found!")

    def find_event_by_id(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                return event
        return None

    def menu(self):
        while True:
            print("\nEvent Management System")
            print("1. Create Event")
            print("2. View Events")
            print("3. Update Event")
            print("4. Delete Event")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_event()
            elif choice == '2':
                self.read_events()
            elif choice == '3':
                self.update_event()
            elif choice == '4':
                self.delete_event()
            elif choice == '5':
                print("Exiting Event Management System...")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    system = EventManagementSystem()
    system.menu()
