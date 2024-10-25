import random
import pandas as pd


def employees_list(file_path):
    df = pd.read_excel(file_path)
    return df.iloc[:, 0].tolist()
employees= employees_list (r"/Users/irisvirus/Desktop/Becode/Manel Bytemind/ByteMind/bouman_8.xlsx")
print(employees)

tables = [[None for _ in range(4)] for _ in range(6)]
print(tables)
print(len(employees))

class Openspace():
    def __init__(self, number_of_tables=6, seats_per_table=4):
        self.number_of_tables = number_of_tables
        self.seats_per_table = seats_per_table
        self.tables = [number_of_tables(seats_per_table) for _ in range(number_of_tables)] 

    def organize(self, names):
        available_names = names.copy()
        random.shuffle(available_names)    
    name_index = 0  
    
    for table in self.tables: 
        for seat in table.seats: 
            if name_index < len(available_names):        
                seat.occupant = available_names[name_index]        
                name_index += 1
            else:        
            seat.occupant = "Empty"