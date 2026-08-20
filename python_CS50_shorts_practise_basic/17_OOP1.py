class thermostat:
    def __init__(self, brand, temp):
        self.brand = brand
        self.temp = temp

    def increase_temp(self, amount):
        self.temp += amount
        print(f"temperature increased by {amount} it is now {self.temp}")

    def decrease_temp(self, amount):
        self.temp -= amount
        print(f"temperature decreased by {amount} it is now {self.temp}")
        if self.temp < 5:
            print("Warning the place is too cold")

controller_brand = input("please enter the controllers brand: ")
controller_temperature = int(input("please enter the places currnet temperature: "))
controller = thermostat(controller_brand, controller_temperature)

amount = int(input("please enter how much degrees that you want to increase the place: "))
controller.increase_temp(amount)
amount = int(input("please enter how much degrees that you want to decrease the place: "))
controller.decrease_temp(amount)