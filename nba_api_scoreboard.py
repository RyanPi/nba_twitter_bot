from nba_api.live.nba.endpoints import scoreboard
import pprint
# from nba_api.stats.endpoints import winprobabilitypbp
scoreboard = scoreboard.ScoreBoard()
scoreboard_dict = scoreboard.get_dict()

gameIDs =[]
counter=0
for game in scoreboard_dict["scoreboard"]["games"]:
    gameIDs.append(game["gameId"])
    homeTeamTri = game["homeTeam"]["teamTricode"]
    homeTeamScore = game["homeTeam"]["score"]
    awayTeamTri = game["awayTeam"]["teamTricode"]
    awayTeamScore = game["awayTeam"]["score"]
    print("GameID:", gameIDs[counter])
    print(homeTeamTri, homeTeamScore)
    print(awayTeamTri, awayTeamScore)
    print("------------")
    counter+=1

    

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(scoreboard_dict)