number = int(input("please enter how many scores that you want to enter: "))
scores = []
for i in range(number):
    point = int(input("please enter the point: "))
    scores.append(point)
scores.sort()
print(scores)
scores.reverse()
print(scores)
target = int(input("please enter the number that you want to count how many times that it repeat in list: "))
print(f"{target} is repeated {scores.count(target)} times")
target = int(input("please enter the number that you want to look for which index that is"))
print(f"{target} is in index {scores.index(target)} ")