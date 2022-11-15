import os
import random

def Roll(player:tuple) -> tuple:
    name = player[0]
    money = player[1]
    hp = player[2]
    potions = player[3]

    while True:
        #делаем ссылки на статы героя
        os.system("cls")
        print("персонаж")
        print("name", name)
        print("money", money)
        print("hp", hp)
        print("СКОЛЬКО ЗЕЛЕК", potions)
        print(name, "приехал к роботу")
        print("К Абатуру приехал землянин, Абатур должен вызвать играть кости землянина, если он откажеться, станет сгустком эсенции или образцом для опытов")
        print("1 = играть")
        print("0 = играть?")
        answe = input("введите номер карты и нажмите ENTER")
        if answe == 1 or 0:
            os.system("cls")
            hiddennumber = random.radint(1,100)
            attempts = 6
            input("++++++")
            while attempts > 0:
                number = input("введите число, смертное")
                if number == hiddennumber:
                    print("Система говорит, что число равно моему. Поздравляю смертный, Абатур дарит тебе жизнь и бутылка пива")
                    break
                elif number > hiddennumber:
                    print("Система говорит, что число больше моего ")
                    attempts -= 1
                    print(f"Система говорит, что у вас снялась попытка")
                else:
                    print("Система говорит, что число меньше моего ")
                    attempts -= 1
                    print(f"Система говорит, что у вас снялась попытка")
                break
            if attempts > 0:
                return (name, money, hp, potions)
                break
            else:
                hp -= 200
                return (name, money, hp, potions)
                break




        else:
            hp -= 200
            return (name, money, hp, potions)

            #FIXME НЕ запускается локация и не снимает хп


