import random


names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Isabel", "Jack", "Kelly", "Liam"]


random.shuffle(names)


tables = [[None for _ in range(4)] for _ in range(6)]


name_index = 0  


for table_index in range(6):
    for seat_index in range(4):
        if name_index < len(names):
            tables[table_index][seat_index] = names[name_index]
            name_index += 1
        else:
            tables[table_index][seat_index] = "Empty"  
for i, table in enumerate(tables, 1):
    print(f"Table {i}: {table}")
