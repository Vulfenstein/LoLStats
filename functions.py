from riotwatcher import LolWatcher, ApiError
import constants

import requests

def getStats(summonerId):
    results = constants.lol_watcher.summoner.by_name(constants.my_region, str(summonerId))
    return results

def getGameStats(summonerId):
    results = constants.lol_watcher.spectator.by_summoner(constants.my_region, str(summonerId))
    return results

def getChampion(championId):
    r = requests.get(constants.url)
    json_obj =r.json()
    data = json_obj['data']
    for name, attributes in data.items():
        if attributes['key'] == str(championId):
            return name
    #print(data_json)