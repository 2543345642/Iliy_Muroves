import os
import random


user_name = input("введите имя")
user_hp = 100

enemy_hp = 100
enemy_name = "Жран Борзый"

print("сражение")
input("enter - дальше")

while user_hp > 0 and enemy_hp > 0:
    os.system("cls")

    user_attack = random.randint(1, 10)
    enemy_hp -= user_attack
    print(f"{user_name} ударил {enemy_name} на {user_attack} и оставил {enemy_hp}")

    if user_hp < 0: 
        break
    


    enemy_attack = random.randint(1, 10)
    user_hp -= enemy_attack
    print(f"{enemy_name} ударил {user_name} на {enemy_attack} и оставил {user_hp}")
    input("enter - дальше")

    if enemy_hp < 0: 
        break


if user_hp < 0: 
    print(f"победил {user_name}")
else:
    print(f"поражение")