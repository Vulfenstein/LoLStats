class Account:
    def __init__(self, id, accountId, puuid, name, summonerLevel, champion):
        self.id = id
        self.accountId = accountId
        self.puuid = puuid
        self.name = name
        self.summonerLevel = summonerLevel
        self.champion = champion

    def setChampion(self, champion):
        self.champion = champion

class PlayerInfo:
    def __init__(self, name, teamId, championId):
        self.name = name
        self.teamId = teamId
        self.championId = championId

    
        
