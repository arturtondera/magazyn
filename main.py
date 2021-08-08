from tabulate import tabulate
import csv
from csv import DictReader

Pots ={"name": "Pots",
         "quantity": 4,
         "unit": "szt",
         "unit_price": 10}
Apples ={"name": "Apples",
         "quantity": 14,
         "unit": "kg",
         "unit_price": 3}        
Tanks ={"name": "Tanks",
         "quantity": 1,
         "unit": "szt",
         "unit_price": 10000}
items = [Pots, Apples, Tanks]
headers = ["Name", "Quantity", "Unit", "Unit Price (PLN)"]
sold_items = []
def load_items_from_csv():
    with open('magazyn.csv', 'r') as read_obj:
      dict_reader = DictReader(read_obj)
      items = list(dict_reader)
    print(items)
def get_items():
  print(items)
  print(tabulate(((i["name"], i["quantity"], i["unit"], i["unit_price"]) for i in items), headers, tablefmt="grid"))
def add_item():
  new_item = {}
  new_item["name"] = input("Item name: ")
  new_item["quantity"] = int(input("Item quantity: "))
  new_item["unit"] = input("Add unit: ")
  new_item["unit_price"] = int(input("Add price: "))
  items.append(new_item)
def sell_item():
  sold_item = input("Item name: ")
  if any(d['name']== sold_item for d in items):
    sold_quantity = int(input("Quantity sold: "))
    for entry in items:
      if entry['name'] == sold_item:
        entry['quantity'] = entry['quantity'] - sold_quantity
        sold_item ={}
        sold_item['name'] = entry['name']
        sold_item['quantity'] = sold_quantity
        sold_item['unit'] = entry['unit']
        sold_item['unit_price'] = entry['unit_price']
        sold_items.append(sold_item)
    return {}
  else:
    print("No such object in storage")
def get_costs():
    cost=[]
    for d in items:
      cost.append(d['quantity'] * d['unit_price'])
    print(sum(cost))
def get_income():
    income=[]
    for x in sold_items:
      income.append(x['quantity'] * x['unit_price'])
    print(sum(income))
def export_items_to_csv():
    keys = items[0].keys()
    with open('magazyn.csv', 'w', newline='')  as output_file:
      dict_writer = csv.DictWriter(output_file, keys)
      dict_writer.writeheader()
      dict_writer.writerows(items)
beginning = input("What would you like to do?")
while beginning != "exit":
  if beginning == "show":
    get_items()
    beginning = input("What would you like to do?")
  if beginning == "add":
    add_item()
    beginning = input("What would you like to do?")
  if beginning == "sell":
    sell_item()
    beginning = input("What would you like to do?")
  if beginning == "sold":
    print(sold_items)
    beginning = input("What would you like to do?")
  if beginning == "cost":
    get_costs()
    beginning = input("What would you like to do?")
  if beginning == "income":
    get_income()
    beginning = input("What would you like to do?")
  if beginning == "save":
    export_items_to_csv()
    beginning = input("What would you like to do?")
  if beginning == "load":
    load_items_from_csv()
    beginning = input("What would you like to do?")  
else: 
  print("Exitting... Bye!")