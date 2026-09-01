# properties -> @ kullnaılacak
# decoraters başka fonksiyonları modifiye etmeye yarayan özellik
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):  #bu objeyi string e çevirmemizi sağlar
        return f"{self.name} from {self.house}"

    @classmethod  # yani obje tanımlanmadan sadece class kullanılarak değer girilebilir
    def get(cls): 
        name = input("name: ")
        house = input("house: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()