import requests
from pprint import PrettyPrinter
import json

BASE_URL = "https://api.sportsdata.io"
API_KEY = "5dfb1139e28a480d9e3f84f84f340c2b"
printer = PrettyPrinter()

date = input("Enter date of MLB game:") # format should be "2017-JUL-31"
team = input("Enter the team that played on that date:") # format should be "NYY"

#####

# we should clean the data above using chatGPT here -> return date, team

#####

# Get Game ID
request_url = f"{BASE_URL}/v3/mlb/stats/json/BoxScores/{date}?key={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    print("successful response")
    games_data = response.json()

print(len(games_data))

game_id = -1

for i in range(len(games_data)):
    if games_data[i]['Game']['HomeTeam'] == team or games_data[i]['Game']['AwayTeam'] == team:
        desired_game_index = i
        game_id = games_data[i]['Game']['GameID']
        break

if game_id == -1:
    print("Game not found in database")
else:
    print(game_id)

#####
request_url3 = f"{BASE_URL}/v3/mlb/scores/json/AllTeams?key={API_KEY}"
# Get play-by-play data for specific game using game_id
request_url2 = f"{BASE_URL}/v3/mlb/pbp/json/PlayByPlay/{game_id}?key={API_KEY}"
response2 = requests.get(request_url3)

if response2.status_code == 200:
    print("successful response")
    pbp_data = response2.json()

printer.pprint(pbp_data)





class Game:
    # constructor
    def __init__(self, game_date, team_abbreviation):
        self.game_id = game_id
        self.standings = None
        self.starting_pitchers = None
        self.scoring_plays = None
        self.pitching_changes = None
        self.Result = None

    def get_team_name(team_abbreviation):
        request_url3 = f"{BASE_URL}/v3/mlb/scores/json/AllTeams?key={API_KEY}"
        if response2.status_code == 200:
            team_data = response2.json()
            for team in team_data:



        
    
    


# data has statistics of every at bat

#####

# Get major statistics from pbp_data for the game
    # Homeruns, Hits, strikeouts

#####

##Need to retrieve the team names from the three letter acronyms