import os
import random

def bitva(player:tuple) -> tuple:

    name = player[0]
    money = player[1]
    hp = player[2]
    potions = player[3]

    enemy_hp = 100
    enemy_name = "Жран Борзый"


    input("enter - дальше")

    while hp > 0 and enemy_hp > 0:
        os.system("cls")

        user_attack = random.randint(1, 10)
        enemy_hp -= user_attack
        print(f"{name} ударил {enemy_name} на {user_attack} и оставил {enemy_hp}")

        if hp < 0:
            break



        enemy_attack = random.randint(1, 10)
        hp -= enemy_attack
        print(f"{enemy_name} ударил {name} на {name} и оставил {hp}")
        input("enter - дальше")

        if enemy_hp < 0:
            break


    if hp > 0:
        print(f"победил {name}")
        return (name, money, hp, potions)
    else:
        print(f"поражение")
        return (name, money, hp, potions)