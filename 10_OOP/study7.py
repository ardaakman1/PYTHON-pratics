import random

class Hat:

    houses = ["asd", "dsa", "ev", "house"]
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")  # artık self kullanmadığımız için (init olmadığı için) direkt Class adıyla metod çağırabilirim