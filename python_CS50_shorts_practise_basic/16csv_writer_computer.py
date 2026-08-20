import csv
import sys
# in this program you should open a CSV file
if len(sys.argv) != 2:
    print("Command-line argument error")
    sys.exit(1)
print()
number = int(input("please enter how many parts that you are going to enter: "))
with open(sys.argv[1], "w", newline='') as file:
    # newline ='' Prevents extra blank lines in CSV files on windows
    headers = ["part_name", "brand", "price"]
    writer = csv.DictWriter(file, fieldnames=headers)
    #  fieldnames is an argument it helps us to define our headers to writer
    writer.writeheader()
    price_sum = 0
    for i in range(number):
        name = input("please enter the parts name: ")
        brand = input("please enter the parts brand: ")
        price = float(input("please enter the parts price: "))
        price_sum += price
        row_to_save = {"part_name":name, "brand":brand, "price":price}
        writer.writerow(row_to_save)
    print(f"total price of your parts is {price_sum}")
print("file written succesfully")

with open(sys.argv[1], "r", newline='') as file:
    reader = csv.DictReader(file)
    print("--------LIST--------")
    for row in reader:
        print(f"parts:{row['part_name']}|||brand:{row['brand']}|||price:{row['price']}")