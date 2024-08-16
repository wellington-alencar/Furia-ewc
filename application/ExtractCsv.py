from model.cs2.Cs2 import findCs2
from model.fc.Fc import findFc
from model.rainbowsix.RainbowSix import findRainbowsix
from model.rocketleague.RocketLeague import findRocketLeague
import csv


def extractCsv():
    matches = []
    cs = findCs2()
    fc = findFc()
    rainbowsix = findRainbowsix()
    rocketLeague = findRocketLeague()

    insertInMatches(cs, matches)
    insertInMatches(fc, matches)
    insertInMatches(rainbowsix, matches)
    insertInMatches(rocketLeague, matches)

    columns = ["Game", "Data", "Torneio", "Oponente", "Placar da Furia", "Placar do Oponente"]
    with open('results.csv', 'w', newline='') as arqCsv:
        writer = csv.DictWriter(arqCsv, fieldnames=columns)
        writer.writeheader()
        writer.writerows(matches)


def insertInMatches(game, matches):
    if game is not None:
        for i in game:
            matches.append(i)
