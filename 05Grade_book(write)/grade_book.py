import csv
import sys
#  open your file as csv
if len(sys.argv) != 2:
    print("Command-line argument error")
    sys.exit(1)
number = int(input("\nHow many students are there in your classroom: "))
with open(sys.argv[1], "w", newline='') as file:
    #  newline ='' Prevents extra blank lines in CSV files on windows
    #  it works like end print("hello", end ="") 
    headers = ["student_name", "midterm_grade", "final_grade"]# header is my variable 
    writer = csv.DictWriter(file, fieldnames=headers) #  writer is my variable
    #  fieldnames is an argument it helps us to define our headers to writer
    writer.writeheader() # this creates the first row of the csv file
    for i in range(number):
        name = input(f"\nPlease enter student {i + 1} name: ")
        midterm_grade = int(input(f"\nPlease enter student {i + 1} midterm grade: "))
        final_grade = int(input(f"\nPlease enter student {i + 1} final grade: "))
        row_to_save = {"student_name": name,"midterm_grade": midterm_grade, "final_grade": final_grade}
        #  we put {} in [] this place in row_to_save because we are defining a dictionary not list
        writer.writerow(row_to_save) #  to write rows except header we write it on the top
print(f"\n\nProcess is completed\n{sys.argv[1]} is created succesfully")
