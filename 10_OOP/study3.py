class Student:
    def __init__(self, name, house):  # bir class içindeki nesneleri kullanıma hazılamak için bu kullanılır YANİ student çağrıldığı gibi içine bunlar yazdırılacak 
        if not name:
            raise ValueError("Missing name")  # eğer bir şey yanlış giderse bunu ekrana getiricez
        if house not in ["asd", "ev", "house", "dsa"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house  # bunlara instance variable denir


def main():
    student = get_student()
    print(f"{student.name}, {student.house}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)


if __name__ == "__main__":
    main()