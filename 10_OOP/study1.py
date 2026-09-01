def main():
    student = get_student()
    print(f"{student[0]}, {student[1]}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    return (name, house)  # böylece tuple yapmış olduk (immutable liste gibi)
 
if __name__ == "__main__":  # eğer bu dosya çalışıtırılırsa main() fonksiyonu çalışcak başka bir dosya ise sadece fonksiyonlar çağrılacak
    main()

# python da C nin aksine return birden fazla değer döndürebilir
