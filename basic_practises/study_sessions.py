try:  # this program will search a word in the file that you re looking for
    target_word = input("Please enter the word that you are looking for: ")
    count = 0
    results = ""
    with open("notes.txt", "r") as file:
        for line in file:
            if target_word in line:  # in is a special membership operator that allows you to look in
                count += 1
                results += line
    if count > 0:
         print(f"\n{target_word} word have found {count} times in your file\n\n")
         print(f"\nthe rows that includes your word:{results}\n")
    else:
        print("\nCould not found any of your word\n\n")

except FileNotFoundError:
    print("You haven't written anything yet...\nSo this will be your first notes!\n")
with open("notes.txt", "a", newline='') as file:
    row_to_save = input("\nplease enter your notes: ")
    file.write(f"{row_to_save}\n")