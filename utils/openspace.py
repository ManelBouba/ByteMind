from table import Table
import random
import pandas as pd

def names_list(file_path):
    df = pd.read_excel(file_path)
    return df.iloc[:, 0].tolist()

# Load names from Excel
names = names_list(r"C:\Users\pc click\Desktop\ByteMind\bouman_8.xlsx")

class Openspace:
    def __init__(self, number_of_tables, seats_per_table):
        """Initializes the Openspace class with tables and seats per table."""
        self.number_of_tables = number_of_tables
        self.tables = [Table(seats_per_table) for _ in range(number_of_tables)]

    def organize(self, names):
        """Randomly assign people to seats across tables."""
        available_names = names.copy()
        random.shuffle(available_names)
        name_index = 0
        
        for table in self.tables:
            for seat in table.seats:
                if name_index < len(available_names):
                    seat.set_occupant(available_names[name_index])  # Use set_occupant for assignment
                    name_index += 1
                else:
                    seat.occupant = "empty"  # Mark remaining seats as empty

    def display(self):
        """Display the seating arrangement."""
        print("\n-+-+-+- SEATING ARRANGEMENT -+-+-+-+-+-\n")
        
        for i, table in enumerate(self.tables, 1):
            print(f"Table {i}:")
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant != "" else "empty"
                print(f"Seat: {occupant}")

    """def store(self, filename):
        #Stores the seating arrangement into an Excel file.
        data = []
        for i, table in enumerate(self.tables, 1):
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant != "" else "Empty"
                data.append((f"Table {i}", occupant))
        
        df = pd.DataFrame(data, columns=['Table', 'Occupant'])
        df.to_excel(filename, index=False)
        print(f"Seating arrangement saved to {filename}")
"""