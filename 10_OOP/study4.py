#  match ve method kullanımı
class Student:
    def __init__(self, name, house, ability):  # bir class içindeki nesneleri kullanıma hazılamak için bu kullanılır YANİ student çağrıldığı gibi içine bunlar yazdırılacak 
        if not name:
            raise ValueError("Missing name")  # eğer bir şey yanlış giderse bunu ekrana getiricez
        if house not in ["asd", "ev", "house", "dsa"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.ability = ability

    def __str__(self):  #bu objeyi string e çevirmemizi sağlar
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.ability:  # python daki switch case
            case "a":
                return ":)"
            case "b":
                return ":|"
            case "c":
                return ":("
            case _:
                return "ability could not found"

def main():
    student = get_student()
    print(student)
    print(student.charm())

def get_student():
    name = input("name: ")
    house = input("house: ")
    ability = input("ability: ")
    return Student(name, house, ability)


if __name__ == "__main__":
    main()