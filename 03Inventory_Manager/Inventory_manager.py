import csv
import sys 
# this program gives information about inventory in a store (it looks to the inventory.csv file)
if len(sys.argv) != 2:
    print("Command-line argument error")
    sys.exit(1)
print()
total_price = 0 # to calculate total price of the inventory
product_count = 0 # to calculate total product type number
with open(sys.argv[1], "r") as file:
    reader = csv.DictReader(file)  # to open file as a dictionary
    for row in reader:
        if int(row["quantity"]) < 10: #  I put int there because row['quantity'] is a string
            print(f"Warning! {row['product']} is low in stock there are just {row['quantity']} left")
            print()
        total_price += int(row['quantity']) * int(row['price']) # I put int because they are strings
        product_count += 1
print(f"There are {product_count} types of products in this store")
print(f"Every thing costs {total_price} in this store")
print()

        