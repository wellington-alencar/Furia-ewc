import json


def convertJson(game):
    json_output = json.dumps(game, indent=4)
    print(json_output)
