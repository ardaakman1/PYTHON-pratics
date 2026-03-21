import csv
import sys
if len(sys.argv) != 3:
    print("command-line argument error")
    sys.exit(1)
count = 0
with open(sys.argv[1], "r") as file:  # argv[1] is the file that program is going to read
    reader = csv.DictReader(file)  
    # I create reader because if I use file = csv.DictReader(file) it would transform file to dictionary
    # we use csv. front of the DictReader because firt we need to define the library
    for row in reader:
        if sys.argv[2] == row["type"]:
            count += 1
            print(f"Movie: {row['title']} | Rating: {row['rating']}")
            # in row['title'] we can write it with "" but it can make python could not understand where string ended 
print()
print(f"{count} movies found!")
