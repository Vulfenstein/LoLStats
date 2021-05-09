from riotwatcher import LolWatcher, ApiError
from accounts import Account
import constants

# Variables
userInfo = []
lol_watcher = constants.lol_watcher
my_region = constants.my_region

# Grab account tags
for x in range(0,1):
    current = lol_watcher.summoner.by_name(my_region, constants.all_users[x])
    userInfo.append(Account(current['id'], current['accountId'], current['puuid'], current['name']))

# Grab current game stats for each player
for user in userInfo:
    try:
        gameStats = lol_watcher.spectator.by_summoner(my_region, user.id)
        print(gameStats)
    except ApiError as err:
        if err.response.status_code == 404:
            print(user.name, " is not playing")
        else:
            print("something went wrong...\n")
            print("Player: ", user.name)
            print("Error code:", err.response.status_code)

# Player history
playerStats = lol_watcher.matches.by_summoner(my_region, user.id, begin_index=0, end_index=0)
print(playerStats)


#print(accounts[0].id)

# all objects are returned (by default) as a dict
##my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
#print(my_ranked_stats)

#my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])

#my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])
#print(my_matches)
