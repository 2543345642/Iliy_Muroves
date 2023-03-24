"""
class Student:
    def __init__(self, name):     #конструктор класса
        print("студент", name,"создан")
        self.name = name # атрибут экземпляра
        self.grades = []

    def get_grade(self, grade: int): #экземплярный метод
        self.grades.append(grade)
        print("студент", self.name,"получил", grade)



student_1 = Student("Вася Питонов")  # создание экземпляра класса
student_1.get_grade(5)
print(student_1.grades)

"""
print("имя:" name)
print("здоровье:" hp_now)
print("здоровье макс:" hp_max)
print("уровень:" lvl)
print("опыт:" xp_now)
print("опыт след:" xp_next)
print("оружие:" weapon)
print("щит:" shield)
print("атака:" attack)
print("защита:" defence)
print("удача:" luck)
print("деньги:" money)
print("инвентарь:" inventory)