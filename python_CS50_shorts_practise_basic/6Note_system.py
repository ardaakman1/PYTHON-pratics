number = int(input("please enter the number of the students in this class: "))
notes = []
for i in range(number):
    score = int(input("please enter the score of the student: "))
    notes.append(score)
passed_notes = [n for n in notes if n >= 60]
average = sum(notes) / len(notes)
print(f"the average of the notes is {average:.2f}")  # :.2f this showes only 2 digits after period
print(f"the highest note in class is {max(notes)}")
print(f"the lowest note in class is {min(notes)}")
print()
print("passed notes:")
print(passed_notes)
notes.sort()
print("sorted notes:")
print(notes)
