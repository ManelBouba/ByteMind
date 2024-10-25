from table import Table
import random


class Openspace():
    def __init__(self, number_of_tables, seats_per_table):
        ''' Initializes the Openspace class.
        - number_of_tables: The number of tables in the room.
        - seats_per_table: The number of seats at each table. As per Table'''
        self.number_of_tables = number_of_tables
        self.tables = [Table(seats_per_table) for _ in range(number_of_tables)] 

    def organize(self, names):
        """Shuffle through the names from document and randomise the order
        If there are more seats than names, the seats remain empty"""
        
        available_names = names.copy()
        random.shuffle(available_names)    
        name_index = 0  
        """Loops through tables and seats at the table"""
        for table in self.tables: 
            for seat in table.seats: 
                if name_index < len(available_names):        
                    table.assign_seat(available_names[name_index])        
                name_index += 1
            else:      
                seat.occupant = "empty"

    def display(self): 
        """Display the seating arrangement."""
        print("\n-+-+-+- SEATING ARRANGEMENT -+-+-+-+-+-\n")
        
        for i, table in enumerate(self.tables, 1):  
            print(f"Table {i}: {table}")
            for seat in table.seats:
                    occupant = seat.occupant if seat.occupant != "" else "empty"
                    print(f"Seat: {occupant}")

    def store(self, filename):
        """Stores the seating arrangement into an Excel file."""
        data = []
        #Loop through tables
        for i, table in enumerate(self.tables, 1):
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant != "" else "Empty"
                data.append((f"Table {i}", occupant))
        
        #Create pandas data frame
        df = pd.DataFrame(data, columns=['Table', 'Occupant'])
        
        # Store in Excel file
        df.to_excel(filename, index=False)
        print(f"Seating arrangement saved to {filename}")