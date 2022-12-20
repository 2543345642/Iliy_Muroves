from random import choice, randint
import os

first_name = ("Жран", "Жмых", "Бром", "Дин", "Ван", "Грим")
last_name = ("Дикий", "Ужасный", "Яросный", "Угрюмый", "Вонючий", "Свирепый", "Старый")


def make_hero(
name=None,
hp_curret=None,
hp_max=20,
lvl=0,
xp_next=None,
xp_curret=0,
ATK_base=3,
ATK_weapon=None,
weapon=None,
defense_base=0,
defense_shield=0,
defense_armor=0,
shield=None,
armor=None,
luck=1,
inventory=None,
money=None,
mage=None,
mp_max=None,
mp_curret=None,
stamina_max=None,
stamina_curret=None
) -> dict:
    if not name:
        name = choice(first_name) + " " + choice(last_name)
    if not money:
        money = randint(1, (5 + 10 * lvl))
    defense_curret = defense_base + defense_shield + defense_armor
    if not inventory:
        inventory = []
    if not xp_next:
        xp_next = 234 + 234 * (lvl * 2)
    if not hp_max:
        hp_max = 20 + 5 * lvl
    if not hp_curret:
        hp_curret = hp_max
    if not ATK_weapon and not weapon:
        ATK_weapon = 0
    ATK_curret = ATK_base + ATK_weapon
    if not mage:
        mage = choice([True, False])
    if mage == True and not mp_max:
        mp_max = 20 + 5 * lvl
    if not stamina_max:
        stamina_max = 20 + 5 * lvl
    if not mp_curret:
        mp_curret = mp_max
    if not stamina_curret:
        stamina_curret = stamina_max



    return {
        "имя":name,
        "хп":hp_max,
        "хп макс":hp_curret,
        "лвл":lvl,
        "оставшийся опыт":xp_next,
        "максимальный опыт":xp_curret,
        "базовая атака":ATK_base,
        "атака оружием":ATK_weapon,
        "атака макс":ATK_curret,
        "оружие":weapon,
        "базовая защита":defense_base,
        "текущая защита":defense_shield,
        "защитная броня":defense_armor,
        "текущее отражение":defense_curret,
        "щит":shield,
        "броня":armor,
        "удача":luck,
        "инвентарь":inventory,
        "деньги":money,
        "маг":mage,
        "мана макс":mp_max,
        "Мана текущая":mp_curret,
        "стамина макс":stamina_max,
        "стамина текущая":stamina_curret
    }

def show_hero(hero):
    name = hero["имя"]
    hp_max = hero["хп"]
    hp_curret = hero["хп макс"]
    lvl = hero["лвл"]
    xp_next = hero["оставшийся опыт"]
    xp_curret = hero["максимальный опыт"]
    ATK_base = hero["базовая атака"]
    ATK_weapon = hero["атака оружием"]
    ATK_curret = hero["атака макс"]
    weapon = hero["оружие"]
    defense_base = hero["базовая защита"]
    defense_shield = hero["текущая защита"]
    defense_armor = hero["защитная броня"]
    defense_curret = hero["текущее отражение"]
    shield = hero["щит"]
    armor = hero["броня"]
    luck = hero["удача"]
    inventory = hero["инвентарь"]
    money = hero["деньги"]
    mage = hero["маг"]
    mp_max = hero["мана макс"]
    mp_curret = hero["Мана текущая"]
    stamina_max = hero["стамина макс"]
    stamina_curret = hero["стамина текущая"]

    print("Персонаж:\n")
    print(f"Имя: {name}")
    if mage == True:
        print("Имеет талант к магии")
    elif mage == False:
        print("Таланта к магии нет")
    print(f"HP: {hp_curret}/{hp_max}")
    if mage == True:
        print(f"MP: {mp_curret}/{mp_max}")
    print(f"Выносливость: {stamina_curret}/{stamina_max}")
    print(f"ATK: {ATK_curret} ({ATK_base} + {ATK_weapon})")
    print(f"Защита: {defense_curret} ({defense_base} + {defense_armor} + {defense_shield})")
    print(f"Удача: {luck}")
    print(f"XP: {xp_curret}/{xp_next}")
    print(f"Уровень: {lvl}")
    print(f"Оружие: {weapon}")
    print(f"Доспехи: {armor}")
    print(f"Щит: {shield}")
    print(f"Монеты: {money}\n")

def levelup(hero: list) -> None:
    while hero["максимальный опыт"] >= hero["оставшийся опыт"]:
        hero["лвл"] += 1
        for i in range(3):
            hero["оставшийся опыт"] = 234 + 234 * (hero["лвл"])
            print(f"Поздравляем! {hero['Имя']} достиг {hero['лвл']} уровня.\n")
            print("Распределите характеристики:\n")
            print(f"1.Увеличить HP {hero['хп макс']}/{hero['хп']} + 5")
            print(f"2.Увеличить ATK {hero['базовая атака']} + 3")
            print(f"3.Увеличить Защиту {hero['базовая защита']} +")
            print(f"4.Увеличить удачу {hero['удача']} + 1")
            print(f"5.Увеличть выносливость {hero['стамина текущая']}/{hero['стамина макс']} + 5")
            if hero["маг"] == True:
                print(f"6.Увеличить ману {hero['Мана текущая']}/{hero['стамина макс']} + 5")
            plus = input("Введите номер выбора и нажмите ENTER: ")
            if plus == "1":
                hero["хп"] += 5
                hero["хп макс"] += 5
            elif plus == "2":
                hero["базовая атака"] += 3
            elif plus == "3":
                hero["базовая защита"] += 2
            elif plus == "4":
                hero["удача"] += 1
            elif plus == "5":
                hero["стамина макс"] += 5
            elif plus == "6" and hero["маг"]:
                hero["стамина макс"] += 5
            if not hero["атака оружием"]:
                hero["атака макс"] = hero["базовая атака"]
            os.system("cls")
            
def buy_item(hero: list, item, price: int) -> None:
    if hero["деньги"] >= price:
        hero["деньги"] -= price
        hero["инвентарь"].append(item)
        print(f"\n{hero['Имя']} купил {item} за {price} монет!")
    else:
        print(f"\n{hero['Имя']} не хватило {price - hero['деньги']} монет!\n")
    input("\nНажмите ENTER чтобы продолжить: ")

def consume_item(hero: list) -> None:
    if not hero["инвентарь"]:
        print("\nИнвентарь:\n\nПустой")
    elif hero["инвентарь"]:
        print("\nИнвентарь:\n")
        options = hero["инвентарь"]
        show_option(hero, options)
        idx = choose_option(hero, options)
        if idx is not None:
            if idx <= len(hero["инвентарь"]) - 1 and idx > -1:
                if hero["инвентарь"][idx] == "Малое зелье лечения":
                    hero["инвентарь"].pop(idx)
                    hero["хп макс"] += 10
                    if hero["хп макс"] > hero["хп"]:
                        hero["хп макс"] = hero["хп"]
                    print(f"\n{hero['Имя']} употребил {hero['инвентарь'][idx]}\n")
                elif hero["инвентарь"][idx] == "Малое зелье маны" and hero["стамина макс"] is not None:
                    hero["инвентарь"].pop(idx)
                    hero["Мана текущая"] += 10
                    if hero["Мана текущая"] > hero["стамина макс"]:
                        hero["Мана текущая"] = hero["стамина макс"]
                    print(f"\n{hero['Имя']} употребил {hero['инвентарь'][idx]}\n")
                elif not hero["стамина макс"]:
                        print("У вас нет таланта к магии чтобы употребить зелье\n")
                elif hero["инвентарь"][idx] == "Малое зелье выносливости":
                    hero["инвентарь"].pop(idx)
                    hero["стамина текущая"] += 10
                    if hero["стамина текущая"] > hero["стамина макс"]:
                        hero["стамина текущая"] = hero["стамина макс"]
                    print(f"\n{hero['Имя']} употребил {hero['инвентарь'][idx]}\n")
                elif hero["инвентарь"][idx] == "Кружка пива":
                    hero["инвентарь"].pop(idx)
                    hero["хп макс"] += 3
                    if hero["хп макс"] > hero["хп"]:
                        hero["хп макс"] = hero["хп"]
                    hero["стамина текущая"] += 5
                    if hero["стамина текущая"] > hero["стамина макс"]:
                        hero["стамина текущая"] = hero["стамина макс"]
                    print(f"\n{hero['Имя']} употребил {hero['инвентарь'][idx]}\n")
                elif hero["инвентарь"][idx] == "Яблоко":
                    pass
                else:
                    print("Предмет нельзя употребить\n")
            else:
                print("Нет такого предмета")

def play_dice(hero: list, bet: int) -> None:
    if bet > 0:
        if hero["деньги"] >= bet:
            hero_score = randint (2, 12)
            casino_score = randint(2, 12)
            print(f"\n{hero['Имя']} выбросил {hero_score}")
            print(f"Ваш противник выбросил {casino_score}\n")
            if hero_score > casino_score:
                hero["деньги"] += bet
                print(f"{hero['Имя']} победил и забирает {bet} монет!\n")
            elif hero_score < casino_score:
                hero["деньги"] -= bet
                print(f"{hero['Имя']} проиграл {bet} монет\n")
            else:
                print("Ничья\n")

        else:
            print(f" У {hero['Имя']} нет столько монет!\n")
    else:
        print("Такая ставка не возможна! Ставки начинааются от 1 монеты!")
    input("Нажмите ENTER чтобы продолжить.")

def start_fight(hero, enemy) -> None:
    text = "Выберите действие:\n"
    while hero["хп макс"] > 0 and enemy[2] > 0:
        os.system("cls")
        show_hero(hero)
        show_hero(enemy)
        print(text)
        options = [
            "Атаковать противника",
            "Использовать предмет из инвентаря"
        ]
        show_option(hero, options)
        option = choose_option(hero, options)
        if option == 0:
            combat_turn(hero, enemy)
        elif option == 1 and hero["инвентарь"]:
            os.system("cls")
            print("Инвентарь:\n")
            consume_item(hero)
        elif option == 1 and not hero["инвентарь"]:
            os.system("cls")
            print("\nИнвентарь пустой\n")
            input("Нажмите ENTER чтобы продолжить бой")
            return start_fight(hero, enemy)
        combat_turn(enemy, hero)
        input("\nНажмите ENTER чтобы продолжить бой: ")
    combat_result(hero, enemy)

def combat_turn(attacker: list, defender: list) -> None:
    if attacker[2] > 0:
        damage = (attacker[8] + randint(0, (attacker[3] + 1)) - defender[13])
        defender[2] -= damage
        print(f"{attacker[0]} атаковал {defender[0]} на {damage}!")

def combat_result(hero: list, enemy: list) -> None:
    os.system("cls")
    if hero["хп макс"] > 0 and enemy[2] <= 0:
        xp = 100 + 100 * enemy[3]
        print(f"{hero['Имя']} победил {enemy[0]} и в награду получает:")
        hero["максимальный опыт"] += xp
        print(f"{xp} опыта")
        hero["деньги"] += enemy[18]
        print(f"{enemy[18]} монет")
        print(f"И забирает предметы: ", end="")
        for item in enemy[17]:
            print(item, end=", ")
        hero["инвентарь"] += enemy[17]
        input("Нажмите ENTER чтобы продолжить: ")
        levelup(hero)
    else:
        print("Вы умерли")

def choose_option(hero: list, options: list) -> int:
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    try:
        option = int(option)
    except ValueError:
        print("\nВвод должен быть целым неотрицательным числом")
        return choose_option(hero, options)
    else: 
        if option <= len(options) - 1 and option > -1:
            return option
        else:
            print("Нет такого выбора")
            return choose_option(hero, options)

def show_option(hero:list, options: list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")

def visit_hub(hero: list) -> None:
    text = f"{hero['Имя']} приехал в город. Чем займёте себя дальше?\n"
    options= [
        "Открыть инвентарь",
        "Зайти к алхимику",
        "Зайти в таверну",
        "Выйти за городские стены",
        "Использовать расходуваемый предмет",
        "Выйти в главное меню"    
    ]
    option = visit(hero, text, options)
    if option == 0:
        return show_inventory(hero)
    if option == 1:
        return visit_alhimist(hero)
    if option == 2:
        return visit_taverna(hero)
    elif option == 3:
        return magic_forest(hero)
    if option == 4:
        consume_item(hero)
    if option == 5:
        print("By")
    input("\nНажмите ENTER чтобы продолжить")

def visit_alhimist(hero: list) -> None:
    text = f"{hero['Имя']} зашёл в лавку ахимика. Здесь продаются зелья и ингридиенты.\n\nАлхимик: Прибыл прикупить зелья? Всё на витрине, выбирай:\n"
    options = [
        "Купить малое зелье лечения за 5 монет",
        "Купить малое зелье выносливости за 5 монет",
        "Купить малое зелье маны за 10 монет",
        "Купить лечебную траву за 3 монеты",
        "Выйти из лавки обратно в город"
    ]
    option = visit(hero, text, options)
    if option == 0:
        buy_item(hero, "Малое зелье лечения", 5)
        return visit_alhimist(hero)
    if option == 1:
        buy_item(hero, "Малое зелье выносливости", 5)
        return visit_alhimist(hero)
    if option == 2:
        buy_item(hero, "Малое зелье маны", 10)
        return visit_alhimist(hero)
    if option == 3:
        buy_item(hero, "Лечебная трава", 3)
        return visit_alhimist(hero)
    if option == 4:
        print(f"\n{hero['Имя']} вышел из лавки алхимика.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_hub(hero)

def visit_taverna(hero: list) -> None:
    text = f"{hero['Имя']} зашёл в таверну. Здесь можно поговорить с посетителями, сыграть в кости и арендовать комнату."
    options = [
        "Сыграть в кости",
        "Поговорить с хозяином таверны",
        "Поговорить с Эльфом за правым столиком",
        "Поговорить с незнакомцем в чёрном капишоне за столиков в углу",
        "Поговорить с рыцарями на втором этаже",
        "Поговорить с пьяным гномом за барной стойкой",
        "Поговорить с человеком за левым столиком",
        "Использовать расходуваемый предмет",
        "Выйти из таверны обратно в город"
    ]
    option = visit(hero, text, options)
    if option == 0:
        bet = int(input("Введите желаемую ставку: "))
        play_dice(hero, bet)
        return visit_taverna(hero)
    if option == 1:
        text = "Вы начали диалог с хозяином таверны:\n\nХозяин таверны: Здравствуй путник, в этой таверне ты можешь выпить или же арендовать себе комнату.\n"
        options = [
            "Купить выпивку",
            "Арендовать комнату",
            "Закончить диалог"
        ]
        option = visit(hero, text, options)
        if option == 0:
            buy_pivo(hero)
        if option == 1:
            arenda(hero)
        if option == 2:
            return visit_taverna(hero)
    if option == 2:
        print(f"\n{hero['Имя']} поговорил с Эльфом.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 3:
        print(f"\n{hero['Имя']} поговорил с незнакомцем.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 4:
        print(f"\n{hero['Имя']} поговорил с рыцарями")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 5:
        print(f"\n{hero['Имя']} поговорил с гномом.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 6:
        print(f"\n{hero['Имя']} поговорил с человеком.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 7:
        if not hero["инвентарь"]:
            text = "Инвентарь:\n\nПусто"
        else:
            text = "Инвентарь:\n"
        options = hero["инвентарь"]
        idx = visit(hero, text, options)
        if idx:
            consume_item(hero, idx)
    if option == 8:
        print(f"\n{hero['Имя']} вышел из таверны.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_hub(hero)

def buy_pivo(hero: list) -> None:
    text = "Хозяин таверны: что будете брать?\n"
    options = [
        "Купить кружку пива за 5 монет",
        "Купить медовуху за 10 монет",
        "Купить бутылку эля за 7 монет",
        "Купить бутылку вина за 10 монет",
        "Закончить диалог"
    ]
    option = visit(hero, text, options)
    if option == 0:
        buy_item(hero, "Кружка пива", 5)
        return buy_pivo(hero)
    if option == 1:
        buy_item(hero, "Медовуха", 10)
        return buy_pivo(hero)
    if option == 2:
        buy_item(hero, "Бутылка эля", 7)
        return buy_pivo(hero)
    if option == 3:
        buy_item(hero, "Бутылка вина", 10)
        return buy_pivo(hero)
    if option == 4:
        return visit_taverna(hero)

def arenda(hero: list) -> None:
    print(f"\n{hero['Имя']} арендовал комнату.")
    input("\nНажмите ENTER чтобы продолжить: ")
    return visit_taverna(hero)

def show_inventory(hero: list) -> None:
    os.system("cls")
    print("Инвентарь:\n")
    for num, option in enumerate(hero["инвентарь"]):
        print(f"{num}.{option}")
    if not hero["инвентарь"]:
        print("Пустой\n")
    else:
        print(" ")
    input("Нажмите ENTER чтобы закрыть инвентарь: ")
    return visit_hub(hero)

def magic_forest(hero:list) -> None:
    text = f"\n{hero['Имя']} прибыл ко входу в лес.\n"
    options = [
        "Вернуться в город",
        "Пойти в холмистые поля(lvl 0-3)",
        "Пойти в окрестности зелёного леса(lvl 2-5)"
    ]
    if hero["лвл"] > 3:
        options.append(
            "Пойти в глубь зелёного леса(lvl 4-6)"
        )
    if hero["лвл"] > 5:
        options.append(
            "Пойти в горы(lvl 5-8)"
        )
    if hero["лвл"] > 7:
        options.append(
            "Пойти в горные пещеры(lvl 7-10)"
        )
    if hero["лвл"] > 9:
        options.append(
            "Пойти в окрестности опасного магического леса(lvl 9-12)"
        )
    if hero["лвл"] > 11:
        options.append(
            "Пойти в глубь магического леса(lvl 11-14)"
        )
    if hero["лвл"] > 13:
        options.append(
            "Пойти в подземелье в глубине леса(lvl 13-???)"
        )
    option = visit(hero, text, options)
    if option == 0:
        return visit_hub(hero)
    elif option == 1:
        os.system("cls")
        print(f"{hero['Имя']} пришёл в холмистые поля\n")
        print("На вас напала слизь!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        slime = make_hero(name="Слизь", hp_max=20, lvl=randint(0, 3), stamina_max=20, mage=False)
        start_fight(hero, slime)
        return magic_forest(hero)

    elif option == 2:
        os.system("cls")
        print(f"{hero['Имя']} зашёл в окрестности зелёного леса\n")
        print("На вас напал гоблин!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        goblin = make_hero(name="Гоблин", hp_max=35, lvl=randint(2, 5), stamina_max=35, defense_base=1, mage=False)
        start_fight(hero, goblin)
        return magic_forest(hero)
    elif option == 3 and hero["лвл"] > 3:
        os.system("cls")
        print(f"{hero['Имя']} зашёл в глубь зелёного леса\n")
        print("На вас напал хоб гоблин!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        hob_goblin = make_hero(name="Хоб гоблин", hp_max=50, lvl=randint(4, 6), stamina_max=50, defense_base=3, ATK_weapon=2, mage=False)
        start_fight(hero, hob_goblin)
        return magic_forest(hero)
    elif option == 4 and hero["лвл"] > 5:
        os.system("cls")
        print(f"{hero['Имя']} пришёл в горы\n")
        print("На вас напал циклоп!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        Cyclops = make_hero(name="Циклоп", hp_max=65, lvl=randint(5, 8), stamina_max=65, defense_base=5, ATK_weapon=5, mage=False)
        start_fight(hero, Cyclops)
        return magic_forest(hero)
    elif option == 5 and hero["лвл"] > 7:
        os.system("cls")
        print(f"{hero['Имя']} вы зашли в пещеры\n")
        print("На вас напала гиганская летучая мышь!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        bat = make_hero(name="Гиганская летучая мышь", hp_max=85, lvl=randint(7, 10), stamina_max=85, defense_base=3, ATK_weapon=10)
        start_fight(hero, bat)
        return magic_forest(hero)
    elif option == 6 and hero["лвл"] > 9:
        os.system("cls")
        print(f"{hero['Имя']} зашёл в окрестности опасного магического леса\n")
        print("На вас напал лютый волк!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        wolf = make_hero(name="Лютый волк", hp_max=100, lvl=randint(9, 12), stamina_max=100, defense_base=7, ATK_weapon= 10)
        start_fight(hero, wolf)
        return magic_forest(hero)
    elif option == 7 and hero["лвл"] > 11:
        os.system("cls")
        print(f"{hero['Имя']} зашёл в глубь магического леса\n")
        print("На вас напал шипастый медведь!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        bear = make_hero(name="Шипастый медведь", hp_max=150, lvl=randint(11, 14), stamina_max=150, defense_base=15, ATK_weapon=20)
        start_fight(hero,bear)
        return magic_forest(hero)
    elif option == 8 and hero["лвл"] > 13:
        os.system("cls")
        print(f"{hero['Имя']} зашёл в подземелье в глубине леса\n")
        print("На вас напала горгулья!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        gargoyle = make_hero(name="Каменная горгулья", hp_max=150, lvl=randint(13, 17), stamina_max=150, defense_base=20, ATK_weapon=10)
        start_fight(hero, gargoyle)
        """
        TODO: БОСС
        """
        return magic_forest(hero)

def visit(hero: list, text: str, options: list) -> None:
    os.system("cls")
    show_hero(hero)
    print(text)
    show_option(hero, options)
    option = choose_option(hero, options)
    return option
