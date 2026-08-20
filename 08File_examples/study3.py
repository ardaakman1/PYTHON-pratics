names = []
with open("names.txt") as file:  # when we open a file as read, we do not need to specify "r" by default
    for line in file:
        names.append(line.rstrip()) # we will sort the names but strip of the new lines

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")
# or we can sort file in the first iteration