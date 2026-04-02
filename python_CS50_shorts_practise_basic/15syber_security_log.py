logs = {
    "admin1" : {"login_attempts":6, "country":"a", "is_blocked":True},
    "user1" : {"login_attempts":5, "country":"b", "is_blocked":False},
    "guest" : {"login_attempts":4, "country":"c", "is_blocked":True}
}
user_input_name = input("please enter the name that you want to look its log attempt number: ")
user_input = logs.get(user_input_name)
if user_input:
    print(f"user:{user_input_name}")
    print(f"attempt number:{user_input["login_attempts"]}")
else:
    print("could not found the user")

user_input_name = input("please enter the name that you want to increase (by 1) its log attempt number: ")
user_input = logs.get(user_input_name)
if user_input:
    print(f"user:{user_input_name}")
    user_input["login_attempts"] += 1
    print(f"attempt number:{user_input["login_attempts"]}")
else:
    print("could not found the user")

added_user = input("please enter a new user: ")
log_num = int(input(f"please enter how many times {added_user} tried to login the program: "))
country_name = input("please enter which country that the user connected from: ")
logs[added_user] = {"login_attempts":log_num, "country":country_name, "is_blocked":log_num > 5}

del_name = input("please enter the name that you want delete: ")
if del_name in logs:
    removed_data = logs.pop(del_name)  # pop returns value
    print(f"deleted name:{del_name}|||deleted values:{removed_data}")

for user_name, user_data in logs.items():
    if user_data["is_blocked"]:  # if its True
        print(f"{user_name}-----DANGER")