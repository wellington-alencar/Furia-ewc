import requests
from bs4 import BeautifulSoup
import json


def findFc():
    url = "https://liquipedia.net/easportsfc/Nathansr22/Matches"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    matches_table = soup.find('table', class_='wikitable')
    matches = []

    for row in matches_table.find_all('tr')[1:]:
        cols = row.find_all('td')

        if len(cols) > 0 and cols[3].text.strip() == "Esports World Cup 2024":
            match_info = {
                "Game": "FC",
                "Data": cols[0].text.strip(),
                "Torneio": cols[3].text.strip(),
                "Oponente": cols[8].text.strip(),
                "Placar da Furia": cols[5].text.strip(),
                "Placar do Oponente": cols[7].text.strip()
            }
            matches.append(match_info)

    return matches
