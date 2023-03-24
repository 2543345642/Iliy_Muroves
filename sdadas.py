from random import randint
class Humanoid:
    def __init__(self, name):
        self.name=Вася Питонов,
        self.hp_now=100,
        self.hp_max=100,
        self.lvl=1,
        self.xp_now=0,
        self.attack=1,
        self.defence=1,
        self.money = 10,
player = Humanoid(name = "Вася Питонов")

    def hp_damage(self,damages, name):
        self.hp_now -= damages
        print("Игрок" self.name "получил" damages "урона и осталось у него" self.hp_now )
    def Characteristics_display(self):
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
