import os
import shop # импортируем файл shop.py
#меню


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
    
    player_money = 10
    player_hp = 100
    player_name = input("введите имя")
    player_potions = 1



    is_game = True
    while is_game:
        os.system("cls")

        
        

        
        #показывает инфу перса
        print("игра запущена")
        input("нажмите ENTER чтобы продолжить")
        print("персонаж")
        print(f"name {player_name}")
        print(f"money {player_money}")
        print(f"hp {player_hp}")
        print(f"СКОЛЬКО ЗЕЛЕК {player_potions}")
        

        #камень и пути
        print(f"подъезжает {player_name} к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть(1), кто влево поедет - тому играть в кости(2), а кто прямо поедет - пойдёт к лавке(3), а если назад пойдёшь, конец обретёшь(0 если устал играть)».")
        answer = input("введите номер карты и нажмите ENTER")

        if answer == "1":
            print("поехал драться")
        elif answer == "2":
            print("Поехал играть в кости")
        elif answer == "3":
            shop.shop(player_name, player_money, player_hp, player_potions)

        input("ENTER - дальше")
show_menu()