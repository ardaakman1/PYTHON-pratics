import csv

try:
    print("Here are your old notes: \n\n")
    with open("list.csv") as file:
        rows = csv.DictReader(file)  # DictReader e fieldnames vermedim çünkü filedname vermeyince en üstteki başlıkları okumaz ve direkt ikinci satıra geçer
        for row in sorted(rows, key=lambda row: row["fruit"]):
            print(f"fruit: {row['fruit']}, Price: {row['price']}")
    print()
except FileNotFoundError:
    print("Here is your new notes")
    quantity = int(input("Please enter how many fruits that you are going to buy: "))
    with open("list.csv", "w", newline="") as file:
        headers = ["fruit", "price"]
        rows = csv.DictWriter(file, fieldnames=headers)
        rows.writeheader()
        for _ in range(quantity):
            fruit = input("Please enter a fruits name: ")
            price = float(input(f"Please enter the price of {fruit}: "))
            rows.writerow({"fruit": fruit, "price": price})

user_char = input("Do you want to add something to your notes? ")
if user_char.upper() == 'Y':
    quantity = int(input("Please enter how many fruits that you are going to buy: "))
    with open("list.csv", "a", newline="") as file:  # newline koydum çünkü windows csv den ayrı olarak bir daha \n koyuyor bunu engellemek için
        rows = csv.DictWriter(file, fieldnames=["fruit", "price"])
        for _ in range(quantity):
            fruit = input("Please enter a fruits name")
            price = float(input(f"Please enter the price of {fruit}"))
            rows.writerow({"fruit": fruit, "price": price})