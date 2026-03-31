number = int(input("please enter how many tasks that you want to enter your list: "))
tasks = []
for i in range(number):
    task = input("please enter your task: ")
    tasks.append(task)
remove_task = input("please enter which task that you want to delete: ")
try:
    tasks.remove(remove_task)
    print("the task is deleted")
except ValueError:  # I should put this because if the user tries to delete a task that ,s not in the list the program will crush
    print("task could not deleted")
print(f"there are {len(tasks)} tasks in your list")
print()
print(tasks)