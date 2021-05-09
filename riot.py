from riotwatcher import LolWatcher, ApiError
from accounts import Account
import constants
from functions import getStats
from functions import getGameStats
from functions import getChampion

# Variables
friendInfo = []
enemyInfo = []
lol_watcher = constants.lol_watcher
my_region = constants.my_region

# Grab friends account tags
for x in range(0,1):
    current = getStats('SPECTREz')
    friendInfo.append(Account(current['id'], current['accountId'], current['puuid'], current['name'], current['summonerLevel'], ''))

# Grab current game stats
for user in friendInfo:
    try:
        gameStats = getGameStats(user.id)
        # Grab enemy account tags
        for player in range(0,10):
            summoner_name = gameStats['participants'][player]['summonerName']
            champion_id = gameStats['participants'][player]['championId']
            champion = getChampion(champion_id)
            if summoner_name not in constants.all_users:
                current = getStats(summoner_name)
                enemyInfo.append(Account(current['id'], current['accountId'], current['puuid'], current['name'], current['summonerLevel'], champion))
            else: 
                friendInfo[player].setChampion(champion)
    except ApiError as err:
        if err.response.status_code == 404:
            print(user.name, " is not playing")
        else:
            print("something went wrong...\n")
            print("Player: ", user.name)
            print("Error code:", err.response.status_code)


# Grab champions
for user in enemyInfo:
    print(user.name)
    print(user.champion)
