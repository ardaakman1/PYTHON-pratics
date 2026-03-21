import sys
# this program detectes thw words which has more than 5 letters and writes them in to a new file
if len(sys.argv) != 3:  # argv index 1 is the file we will read and index 2 is the file that we are going to write
    print("Command-line argument error")
    sys.exit(1)
count = 0
with open(sys.argv[1], "r") as file:
    with open(sys.argv[2], "w") as new_file:
        for row in file:
            row = row.strip()
            length = len(row)
            if length > 5:
                count += 1
                new_file.write(row + "\n")
print("long words printed to new file!")
print(f"{count} words are found!")

# sys.argv allows us to access file names passed from the terminal
# with opens the file and when the job is done it closes it automatically
# .strip() deletes the'\n' at the end of the file
# in python there are not so much differences (unlike C) between '' and "" they both meaning string
