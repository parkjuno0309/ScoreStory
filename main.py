import requests
from pprint import PrettyPrinter
import json


class Game:
    # constructor
    def __init__(self, game_date, team_abbreviation):
        self.home_pitchers = None
        self.away_pitchers = None
        self.teams = None
        self.game = None
        self.pbp = None
        self.game_date = game_date
        self.team_abbreviation = team_abbreviation
        self.standings = None
        self.starting_pitchers = None
        self.scoring_plays = None
        self.pitching_changes = None
        self.Result = None
        self.BASE_URL = "https://api.sportsdata.io"
        self.API_KEY = "5dfb1139e28a480d9e3f84f84f340c2b"

    def get_team_name(self,abbreviation):
        request_url = f"{self.BASE_URL}/v3/mlb/scores/json/AllTeams?key={self.API_KEY}"
        response = requests.get(request_url)
        if response.status_code == 200:
            team_data = response.json()
            for team in team_data:
                if(team['Active'] == True):
                    if(team['Key'] == abbreviation):
                        return (team['City'] + ' ' + team['Name'])
                    
    def get_player_name(self, id):
        request_url = f"{self.BASE_URL}/v3/mlb/scores/json/Player/{id}?key={self.API_KEY}"
        response = requests.get(request_url)
        if response.status_code == 200:
            data = response.json()
            name = f"{data['FirstName']} {data['LastName']}"
        return name
    
                    
    def get_pbp(self):
        request_url = f"{self.BASE_URL}/v3/mlb/stats/json/BoxScores/{self.game_date}?key={self.API_KEY}"
        response = requests.get(request_url)
        if response.status_code == 200:
            print("successful response")
            games_data = response.json()

        game_id = -1

        for i in range(len(games_data)):
            if games_data[i]['Game']['HomeTeam'] == self.team_abbreviation or games_data[i]['Game']['AwayTeam'] == self.team_abbreviation:
                desired_game_index = i
                game_id = games_data[i]['Game']['GameID']
                break

        if game_id == -1:
            print("Game not found in database")
        
        
        # Get play-by-play data for specific game using game_id
        request_url2 = f"{self.BASE_URL}/v3/mlb/pbp/json/PlayByPlay/{game_id}?key={self.API_KEY}"
        response2 = requests.get(request_url2)

        if response2.status_code == 200:
            #print("successful response")
            pbp_data = response2.json()
            self.pbp = pbp_data['Plays']
            self.game = pbp_data['Game']
                    
    def home_away(self):
        home = self.game['HomeTeam']
        away = self.game['AwayTeam']
        self.teams = {'Home': self.get_team_name(home),'Away': self.get_team_name(away)}

    def get_result(self):
        homeTotalRuns = 0
        homeInningsScored = []
        awayTotalRuns = 0
        a
        innings_data = self.game['Innings']
        for inning in innings_data:
            homeTotalRuns += inning['HomeTeamRuns']
            awayTotalRuns += inning['awayTeamRuns']
        self.Result = {'Home': homeTotalRuns, 'Away': awayTotalRuns}


    def get_pitching_data(self):
        homeid = self.game['HomeTeamStartingPitcherID']
        awayid = self.game['AwayTeamStartingPitcherID']
        homestarter = self.get_player_name(homeid)
        awaystarter = self.get_player_name(awayid)
        home_ids = {}
        away_ids = {}
        home_ids[homeid] = 0
        away_ids[awayid] = 0
        for play in self.pbp:
            if(play['InningHalf'] == 'T'):
                if(play['PitcherID'] != awayid):
                    away_ids[play['PitcherID']] == 0
                    awayid = play['PitcherID']
                else:
                    away_ids[play['PitcherID']] += 1
            else:
                if(play['PitcherID'] != homeid):
                    home_ids[play['PitcherID']] == 0
                    homeid = play['PitcherID']
                else:
                    home_ids[play['PitcherID']] += 1
                    
        
        self.home_pitchers = home_ids
        self.away_pitchers = away_ids

                    
my_instance = Game('2023-APR-30', 'LAD')
my_instance.get_pbp()
my_instance.home_away()
my_instance.get_pitching_data()
print(my_instance.home_pitchers)





        
    
    


# data has statistics of every at bat

#####

# Get major statistics from pbp_data for the game
    # Homeruns, Hits, strikeouts

#####

##Need to retrieve the team names from the three letter acronyms