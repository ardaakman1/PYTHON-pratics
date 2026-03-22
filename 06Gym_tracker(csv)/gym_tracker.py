import csv
import sys 
#  this program will take your gym informations and make them a csv file
if len(sys.argv) != 2:
    print("Command_line error")
    sys.exit(1)
number = int(input("How many execise did you do today? ")) #  I used int because I used range in the loop
with open(sys.argv[1], "w", newline='') as file:
    headers = ["exercise_name", "sets", "reps", "weight(kg)"]
    writer = csv.DictWriter(file ,fieldnames=headers) #  fieldnames = headers of the file 
    writer.writeheader() #  this will write headers of the file
    for i in range(number):
        name = input(f"please enter the exercise {i + 1}'s name: ")
        sets = int(input(f"please enter the exercise {i + 1}'s set number: "))
        reps = int(input(f"please enter the exercise {i + 1}'s rep number: "))
        weight = int(input(f"please enter how much weight did you work with at exercise {i + 1}: "))
        row_to_save = {"execise_name": name, "sets": sets, "reps": reps, "weight(kg)": weight} #  we use {} because we defined dictionary
        writer.writerow(row_to_save)
print(f"\n\nProcess is completed\n{sys.argv[1]} is created succesfully")

