import csv
import sys
# In this program you should open a new file that you are going to write the list
if len(sys.argv) != 2:
    print("Command-line argument error")
    sys.exit(1)
print()
number = int(input("How many items that you want to buy?"))
with open (sys.argv[1], "w", newline = '') as file: 
    # newline ='' Prevents extra blank lines in CSV files on windows
    headers = ["item", "count"] #  the headers of the CSV
    writer = csv.DictWriter(file, fieldnames=headers) # writer is my variable 
    #  fieldnames is an argument it helps us to define our headers to writer
    writer.writeheader() #  this creater the first row of the CSV file
    for i in range(number):
        name = input(f"please enter the item {i + 1}    ")
        amount = int(input(f"please enter the amount of the item {i + 1}    "))
        row_to_save = {"item" : name, "count" : amount} #  row_to_save is a variable
        #  we use ':' instead of '=' because dictionaries are defined with colons
        #  CRITIC: Create a dictionary to map user input to the CSV fieldnames
        writer.writerow(row_to_save)
print(f"\n\nProcess is completed\n{sys.argv[1]} is created succesfully")
