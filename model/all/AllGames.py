from model.cs2.Cs2 import findCs2
from model.fc.Fc import findFc
from model.rocketleague.RocketLeague import findRocketLeague
from model.rainbowsix.RainbowSix import findRainbowsix


def findAll():
    print("================ Jogos da Furia no CS2 ================")
    findCs2()
    print("================ Jogos da Furia no Rainbow Six Siege ================")
    findRainbowsix()
    print("================ Jogos da Furia no FC ================")
    findFc()
    print("================ Jogos da Furia no Rocket League ================")
    findRocketLeague()

