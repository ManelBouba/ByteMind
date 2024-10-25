from openspace import Openspace
from file_utils import List, check_capacity  # Ensure these match exactly with file_utils
from table import Table, Seat

# Configuration
number_of_tables = 6
seats_per_table = 4

# Load names from Excel
names_list_extract = List()
names = names_list_extract.names_list(r"C:\Users\pc click\Desktop\ByteMind\bouman_8 - Short_list.xlsx")

# Check capacity to ensure the seating arrangement can be accommodated
capacity_message=check_capacity(number_of_tables, seats_per_table, names)
print(capacity_message)

# Initialize Openspace with tables and seats configuration
openspace = Openspace(number_of_tables, seats_per_table)

# Organize seating for the provided names
openspace.organize(names)

# Display seating arrangement in console
openspace.display()

# Store the seating arrangement in an Excel file
openspace.store(r"C:\Users\pc click\Desktop\ByteMind\seating_arrangement.xlsx")