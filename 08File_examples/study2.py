name = input("What is your name: ")
with open("names.txt", "a") as file:  # When we use with we do not need to close the file
    file.write(f"{name}\n")
with open("names.txt", "r") as file:  # we can read the file with "r"
    lines = file.readlines()
for line in lines:
    print("Hello,", line.rstrip())  # or we can use end="" instead of rstrip()
print()
with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line, end="")