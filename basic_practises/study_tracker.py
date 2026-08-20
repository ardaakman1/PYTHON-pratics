try:
    count = 0  # row count
    with open("study_sessions.txt", "r") as file:
        for row in file:
            count += 1
    print(f"you have entered {count} rows in this file")
except FileNotFoundError:
    print("You haven't written anything yet...\nSO this will be your first code!\n\n")
row_to_save = input("what did you study today? ")
level = int(input("what is your energy level today? "))
with open("study_sessions.txt", "a", newline='') as file:
    file.write(f"{row_to_save}----Energy level:{level}\n")