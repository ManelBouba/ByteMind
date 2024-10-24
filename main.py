import random
import pandas as pd
tables = [[None for _ in range(4)] for _ in range(6)]
print(tables)
def employees_list(file_path):
    df = pd.read_excel(file_path)
    return df.iloc[:, 0].tolist()
employees=employees_list(r"C:\Users\pc click\Desktop\ByteMind\bouman_8.xlsx")
print(employees)