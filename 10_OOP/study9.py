# inheritence -> bir class ın başka bir class tan variable çekmesi

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):  # Wizard super class oldu Student ı çağırdığımda wizard daki tüm var ları çağıracak
    def __init__(self, name, house):
        super().__init__(name)  # burdaki olay şu super() süper class ı (Wizard) belirtiyor ve bununla super a name i yollamış oluyoruz
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Kamil", "martial arts")