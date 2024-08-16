from model.cs2.Cs2 import findCs2
from model.fc.Fc import findFc
from model.rainbowsix.RainbowSix import findRainbowsix
from model.rocketleague.RocketLeague import findRocketLeague
from model.all.AllGames import findAll


def panel():
    menu()
    option = int(input("Digite a opção desejada: "))
    match option:
        case 1:
            print("================ Jogos da Furia no CS2 ================")
            findCs2()
        case 2:
            print("================ Jogos da Furia no FC ================")
            findFc()
        case 3:
            print("================ Jogos da Furia no Rainbow Six Siege ================")
            findRainbowsix()
        case 4:
            print("================ Jogos da Furia no Rocket League ================")
            findRocketLeague()
        case 5:
            findAll()


def menu():
    print("Escolha uma opção: ")
    print("1 - Jogos da Furia no CS2")
    print("2 - Jogos da Furia no FC")
    print("3 - Jogos da Furia no Rainbow Six Siege")
    print("4 - Jogos da Furia no Rocket league")
    print("5 - Todos os jogos da Furia")














