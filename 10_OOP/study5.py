# properties -> @ kullnaılacak
# decoraters başka fonksiyonları modifiye etmeye yarayan özellik
class Student:
    def __init__(self, name, house):  # bir class içindeki nesneleri kullanıma hazılamak için bu kullanılır YANİ student çağrıldığı gibi içine bunlar yazdırılacak 
        if not name:
            raise ValueError("Missing name")  # eğer bir şey yanlış giderse bunu ekrana getiricez
        self.name = name
        self.house = house

    def __str__(self):  #bu objeyi string e çevirmemizi sağlar
        return f"{self.name} from {self.house}"

    # getter
    @property
    def house(self):  # burdaki house fonksiyonu ile instance variable ın ismi aynı olamaz bu yüzden self._house yapmalıyız
        return self._house  # burda _house 

    # setter
    @house.setter  # bu eğer yazlımıcı değer atarken (farklı bir yerde) hata yaprsa değiştirmesini engeller
    def house(self, house):
        if house not in ["asd", "dsa", "ev", "house"]:
            raise ValueError("Invalid house")
        self._house = house  # ve burda _house

def main():
    student = get_student()
    # student.house = "qwe" burası hata verecek stter dan dolayı   ve buraya _house yazsaydık class içindeki değeri değiştirebilirdik
    print(student)


def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)


if __name__ == "__main__":
    main()