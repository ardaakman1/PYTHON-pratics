
students = []
with open("students.csv") as file:
    for line in file:
        if "," not in line:
            continue
        name, house = line.strip().split(",")
        student = {"name": name, "house": house}  # make it dictionary
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):  # sorted(students["name"]) this will give error
    # because it is a list not a dictionary (it's elemants are dictionarires)
    # python allows you to pass functions as arguments into other functions
    print(f"{student['name']} is in {student['house']}")

# or we can use lambda functions
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
