import sys

try:
    with open("notes.txt", "r") as file:
        print("\n\nYour old Notes:")
        print(file.read())
        print("----------------")
except FileNotFoundError: #  !! if the file could not found or open python will return this error
    print("file could not found...")
    print("this will be your first note!")
    
new_note = input("please enter todays notes:")
with open("notes.txt", "a") as file:
    file.write(new_note + '\n') # I added \n because new notes should be in a new row

print("your note added succesfully!")
