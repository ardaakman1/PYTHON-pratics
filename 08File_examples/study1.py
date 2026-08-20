#  these are form CS50P
name = input("What is your name: ")
file = open("names.txt", "w")  # because of write this code will delete old name and write the new name the user has written
file.write(name)
file.close()  # we should close the file when we don't use with