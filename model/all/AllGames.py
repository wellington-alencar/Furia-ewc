from model.cs2.Cs2 import findCs2
from model.fc.Fc import findFc
from model.rocketleague.RocketLeague import findRocketLeague
from model.rainbowsix.RainbowSix import findRainbowsix
from utilities.ConvertToJson import convertJson


def findAll():
    print("================ Jogos da Furia no CS2 ================")
    convertJson(findCs2())
    print("================ Jogos da Furia no Rainbow Six Siege ================")
    convertJson(findRainbowsix())
    print("================ Jogos da Furia no FC ================")
    convertJson(findFc())
    print("================ Jogos da Furia no Rocket League ================")
    convertJson(findRocketLeague())
