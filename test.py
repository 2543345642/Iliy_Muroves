from main import *


os.system("cls")
player = make_hero(name = "Вася Питонов")
game = visit_hub
while game:
    visit_hub(player)