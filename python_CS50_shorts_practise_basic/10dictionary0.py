car = {  # we define dictionaries with {}
    "brand":"audi",  # keys and values
    "model":"2000",
    "color":"black"
}

car_model = car["model"]
print(f"the car's model is {car_model}")
car["color"] = "red"  # we can cahnge values by this
print(f"the car's color is {car['color']}")  # I used 'color' (same as "color") because it is recomended

km_inform = car.get("km") # if you did not enter anything this will return None
print(f"Mileage of the car:{km_inform}")
km_inform = car.get("km", "there is not any information that entered")  # if you inform (enter) than it will return your information
print(f"Mileage of the car:{km_inform}")

categories = car.keys()
print(categories)
categories = car.values()
print(categories)
for k, v in car.items():
    print(f"keys:{k}||values:{v}")
if "brand" in car:  # this returns true or false
    print("this car has a brand")
car.update({"year":2003})  # this is recomended way if you want it you can do also this car["year"] = 2003
del car["year"]  # this will delete this data from dictionary
car["year"] = 2003
deleted_year = car.pop("year")  # this will delete this data and add it into a new variable
print(f"car was bought in {deleted_year}")
length_of_dict = len(car)  # this counts all key/values pairs
print(f"There are {length_of_dict} datas in the dictionary")

squares = {x: x**2 for x in range(1, 6)}
print(squares)

car.clear()
print(car)