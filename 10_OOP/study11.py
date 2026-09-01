class Spaceship:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        if fuel < 0 or fuel > 100:  # burda daha self._fuel oluşturlmadı fuel ı kontrol etmeliyiz
            raise ValueError("Invalid fuel value")
        self._fuel = fuel

    @classmethod
    def get(cls):
        name = input("name: ")
        fuel = int(input("fuel: "))
        return cls(name, fuel)

    def __str__(self):  # str içine bir şeyler yazmaya gerk yok class içindeki her şeye ulaşabilir
        return f"{self.name} - fuel: {self.fuel}"

class Warship(Spaceship):
    def __init__(self, name, fuel):
        super().__init__(name, fuel)

class Cargoship(Spaceship):
    def __init__(self, name, fuel, cargo_weight):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight

    
    def __str__(self):
        return f"{self.name} - {self.fuel} - {self.cargo_weight}"
    
def main():
    spaceship = Spaceship.get()
    cargo = Cargoship("Titan", 80, 5000)
    print(spaceship)
    print(cargo)

if __name__ == "__main__":
    main()