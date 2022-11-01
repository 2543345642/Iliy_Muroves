import os


def shop(player_name, player_money, player_hp, player_potions):
    while True:
        os.system("cls")
        print("персонаж")
        print(f"name {player_name}")
        print(f"money {player_money}")
        print(f"hp {player_hp}")
        print(f"СКОЛЬКО ЗЕЛЕК {player_potions}")
        print(f"{player_name} приехал в лавку")
        print("1 = купить зелье за 10 монет")
        print("0 = уехать обратно")
        answer = input("введите номер карты и нажмите ENTER")
        if answer == "1":
            os.system("cls")
            if player_money >= 10:
                player_money -= 10
                player_potions += 1
                print("игрок купил зелье")
            elif player_money < 10:
                print("пошёл вон отсюда")
            input("+++++++++++++++")
        return player_money, player_potionsb    

        elif answer == "0":
            break
