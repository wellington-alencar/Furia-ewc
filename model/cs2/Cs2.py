import requests
from bs4 import BeautifulSoup
import json


def findCs2():
    matches = []
    url = "https://liquipedia.net/counterstrike/FURIA_Esports/Matches"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    matches_table = soup.find('table', class_='wikitable')

    for row in matches_table.find_all('tr')[1:]:
        cols = row.find_all('td')
        scores = cols[7].text.split("\xa0: ")
        score_furia = scores[0]

        if ' - ' in score_furia:
            scores_aux = cols[7].text.split(' - ')
            score_furia = scores_aux[0]
            score_opponent = scores_aux[1]
        else:
            score_furia = scores[0]
            score_opponent = scores[1]

        if len(cols) > 0 and cols[6].text.strip() == "Esports World Cup 2024":
            match_info = {
                "Game": "Cs2",
                "Data": cols[0].text.strip(),
                "Torneio": cols[6].text.strip(),
                "Oponente": cols[8].text.strip(),
                "Placar da Furia": score_furia,
                "Placar do Oponente": score_opponent
            }
            matches.append(match_info)

    return matches
