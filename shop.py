import os

def shop(player:tuple) -> tuple:
    #делаем ссылки на статы героя
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
        print(name, "приехал в лавку")
        print("1 = купить зелье за 10 монет")
        print("0 = уехать обратно")
        answer = input("введите номер карты и нажмите ENTER")

        #делаем ссылки на статы игрока
        if answer == "1":
            os.system("cls")
            if money >= 10:
                money -= 10  #изменить деньги
                potions += 1
                print("игрок купил зелье") 
            elif money < 10:
                print("пошёл вон отсюда")
            input("+++++++++++++++")
        elif answer == "0":
            return (name, money, hp, potions)