import os
import shop # импортируем файл shop.py
import bitva # импортируем файл bitva.py
import Roll

def show_menu():
    """
    показывает главное меню
    из него вызывается игра или заканчивается программа
    из него завершается вся программа
    TODO: 
        Настройки: цвет текста
        Сохранение/загрузка
    """
    #Главный цикл меню, завершается правильным выбором
    while True:
        os.system("cls")#очистка
        print("1 - начать новую игру")
        print("2 = выйти")
        answer = input("Введите номер ответа и нажмите ENTER ")
        if answer == "1":
            start_game()
            break
        elif answer == "2":
            print("выходим из игры")
            break
    print("Выходим из меню! Пока")      


#запуск программы
def start_game():
    """
    создаёт персонажа:
        player_name - имя игрока
        player_money - деньги игрока,
        player_hp - жизни игрока, >= 0 иначе игра заканчивается
        player_xp - опыт игрока
    запускает игру
    игра контролируется переменной is_game
    """
    #инфа перса
    player_name = input("введите имя")
    player_money = 10
    player_hp = 200
    player_potions = 1
    player = (player_name, player_money, player_hp, player_potions)




    is_game = True
    while is_game:
        os.system("cls")

        #показывает инфу перса
        print("игра запущена")
        input("нажмите ENTER чтобы продолжить")
        print("персонаж")
        print("name", player[0])
        print("money", player[1])
        print("hp", player[2])
        print("СКОЛЬКО ЗЕЛЕК", player[3])
        
        #камень и пути
        print(f"подъезжает", player[0], "к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть(1), кто влево поедет - тому играть в кости(2), а кто прямо поедет - пойдёт к лавке(3), а если назад пойдёшь, конец обретёшь(0 если устал играть)».")
        answer = input("введите номер карты и нажмите ENTER")

        if answer == "1":
            player = bitva.bitva(player)
        elif answer == "2":
            player == Roll.Roll(player)
        elif answer == "3":
            player = shop.shop(player)


        input("ENTER - дальше")
show_menu()