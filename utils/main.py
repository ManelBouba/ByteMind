from openspace import Openspace
from file_utils import List

 # Load names from Excel
names_list_extract=List()
names= names_list_extract.names_list(r"C:\Users\pc click\Desktop\ByteMind\bouman_8.xlsx")

# Initialize Openspace with 6 tables, each with 4 seats
openspace = Openspace(number_of_tables=6, seats_per_table=4)

# Organize seating
openspace.organize(names)

# Display seating arrangement
openspace.display()

# Store seating arrangement in an Excel file
#openspace.store(r"C:\Users\pc click\Desktop\ByteMind\seating_arrangement.xlsx")