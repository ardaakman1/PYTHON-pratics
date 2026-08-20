import csv

name = input("what is your name: ")
home = input("Where is your house: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, filednames=["name", "home"])
    writer.writerow({"name": name, "home": home})