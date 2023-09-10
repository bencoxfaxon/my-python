# Imports

# Globals

available_tables = [1, 2, 3, 4, 5, 6, 7, 8]
customer_dict = {}

# Class

class Customer:
    
    def __init__(self, name, table, status=False):
        self.name = name
        if table in available_tables: self.table = table
        else: self.table = available_tables[0]
        self.status = status
        self.order = []
        customer_dict[self.table] = self
        for tab in available_tables: 
            if tab == self.table:
                available_tables.remove(tab)
    
    def add_order(self, *order):
        for item in order:
            self.order.append(item)
    
    def remove_order(self, *order):
        for item in order:
            if item in self.order: self.order.remove(item)

# Functions

def print_customers():
        for customer in customer_dict:
            print(customer_dict[customer].name)

def clear_customer(table_number):
    available_tables.append(customer_dict[table_number].table)
    del customer_dict[table_number]

def get_customer(table_number):
    return customer_dict[table_number]
     

# Testing

Customer('Ben', 2, False)
Customer('Steve', 2, False)
print(available_tables)
print_customers()
clear_customer(1)
print_customers()
print(available_tables)
get_customer(2).add_order('Hello')
print(get_customer(2).order)


        



