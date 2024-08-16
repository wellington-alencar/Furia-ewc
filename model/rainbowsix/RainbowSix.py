import requests
from bs4 import BeautifulSoup
import json


def findRainbowsix():
    url = "https://liquipedia.net/rainbowsix/FURIA_Esports/Played_Matches"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    matches_table = soup.find('table', class_='wikitable')
    matches = []

    for row in matches_table.find_all('tr')[1:]:
        cols = row.find_all('td')
        scores = cols[5].text.split("\u00a0: ")
        score_furia = scores[0]
        score_opponent = scores[1]
        if len(cols) > 0 and cols[3].text.strip() == "Esports World Cup 2024":
            match_info = {
                "Game":"Rainbow Six Siege",
                "Data": cols[0].text.strip(),
                "Torneio": cols[3].text.strip(),
                "Oponente": cols[6].text.strip(),
                "Placar da Furia": score_furia,
                "Placar do Oponente": score_opponent
            }
            matches.append(match_info)

    return matches
