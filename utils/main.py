from openspace import Openspace
from file_utils import List
from table import Table ,Seat

number_of_tables=6
seats_per_table=4

 # Load names from Excel
names_list_extract=List()
names= names_list_extract.names_list(r"C:\Users\pc click\Desktop\ByteMind\bouman_8 - Short_list.xlsx")
#names= names_list_extract.names_list(r"C:\Users\pc click\Desktop\ByteMind\bouman_8.xlsx")


capacity=number_of_tables* seats_per_table

if capacity < len(names):
     print("too much people")
elif capacity >len(names):
      left_over = capacity - len(names)
      print (f"There are {left_over} seats available")
else:
      print("all the seats are occupid")


# Initialize Openspace with 6 tables, each with 4 seatsls
openspace = Openspace(number_of_tables, seats_per_table)

# Organize seating
openspace.organize(names)

# Display seating arrangement
openspace.display()

# Store seating arrangement in an Excel file
openspace.store(r"C:\Users\pc click\Desktop\ByteMind\seating_arrangement.xlsx")