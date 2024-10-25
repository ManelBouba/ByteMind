import pandas as pd

#from file_utils import List
class List():

    def __init__(self):
        self.names=[]

    def names_list(self,file_path):
        df = pd.read_excel(file_path)
        self.names=df.iloc[:, 0].tolist()
        return self.names

def check_capacity(number_of_tables, seats_per_table,name):
  
    
    capacity = number_of_tables * seats_per_table

    if capacity < len(name):
        return "Too many people for the available seats."
    elif capacity > len(name):
        left_over = capacity - len(name)
        return f"There are {left_over} seats available."
    else:
        return "All seats are occupied."
   
  
