def get_stats(number):
    small = min(number)
    large = max(number)
    return small, large
my_list = [11, 22, 33, 44, 55]
# my_list = ["11", "22", "33", "44", "55"] if I used this program will look their alphabetical order
min_num, max_num = get_stats(my_list)
print(f"the smallest number is {min_num} biggest number is {max_num}")
stats = get_stats(my_list)
print(stats)  # it become a tuple and now it can not be changed
try:
    stats[0] = 0
except TypeError:
    print("tuples can not be changed!")