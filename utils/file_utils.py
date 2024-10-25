import pandas as pd

#from file_utils import List
class List():

    def __init__(self):
        self.names=[]

    def names_list(self,file_path):
        df = pd.read_excel(file_path)
        self.names=df.iloc[:, 0].tolist()
        return self.names

   
  
