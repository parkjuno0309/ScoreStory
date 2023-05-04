import requests
from pprint import PrettyPrinter
import json
import re
import pandas as pd
import ssl


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
        self.innings_scored = None
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
        name = ''
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
        homeInningsScored = {}
        awayTotalRuns = 0
        awayInningsScored = {}
        innings_data = self.game['Innings']
        for inning in innings_data:
            if inning['HomeTeamRuns'] is not None and inning['HomeTeamRuns'] > 0:
                homeTotalRuns += inning['HomeTeamRuns']
                homeInningsScored[inning['InningNumber']] = inning['HomeTeamRuns']
            if inning['AwayTeamRuns'] is not None and inning['AwayTeamRuns'] > 0:
                awayTotalRuns += inning['AwayTeamRuns']
                awayInningsScored[inning['InningNumber']] = inning['AwayTeamRuns']
        self.Result = {'Home': homeTotalRuns, 'Away': awayTotalRuns}
        self.innings_scored = {'Home': homeInningsScored, 'Away': awayInningsScored}


    def get_pitching_data(self):
        homeid = self.game['HomeTeamStartingPitcherID']
        awayid = self.game['AwayTeamStartingPitcherID']
        homestarter = self.get_player_name(homeid)
        awaystarter = self.get_player_name(awayid)
        home_ids = {}
        away_ids = {}
        home_ids[homestarter] = 0
        away_ids[awaystarter] = 0
        for play in self.pbp:
            currentPitcher = self.get_player_name(play['PitcherID'])
            if(play['InningHalf'] == 'B'):
                if(currentPitcher not in away_ids.keys()):
                    away_ids[currentPitcher] = 1
                else:
                    away_ids[currentPitcher] += 1
            if(play['InningHalf'] == 'T'):
                if(currentPitcher not in home_ids.keys()):
                    home_ids[currentPitcher] = 1
                else:
                    home_ids[currentPitcher] += 1
        
        self.home_pitchers = home_ids
        self.away_pitchers = away_ids

    def get_pitching_changes(self):
        homeid = self.game['HomeTeamStartingPitcherID']
        awayid = self.game['AwayTeamStartingPitcherID']
        changes = []
        for play in self.pbp:
            if(play['InningHalf'] == 'B'):
                if(play['PitcherID'] != awayid):
                    changes.append({'Inning': play['InningNumber'], 'Play': play['PlayNumber'], 
                    'Team': self.game['AwayTeam'], 'Old': self.get_player_name(awayid), 
                    'New': self.get_player_name(play['PitcherID'])})
                    awayid = play['PitcherID']
            else:
                if(play['PitcherID'] != homeid):
                    changes.append({'Inning': play['InningNumber'], 'Play': play['PlayNumber'], 
                    'Team': self.game['HomeTeam'], 'Old': self.get_player_name(homeid), 
                    'New': self.get_player_name(play['PitcherID'])})
                    homeid = play['PitcherID']
        self.pitching_changes = changes
    
def print_data(date = '2023-APR-30', team = 'LAD'):
    team = team.upper()
    date = [char.upper() if char.isalpha() else char for char in date]
    date = ''.join(date)
    
    def check_date_format(date):
        pattern = r'^\d{4}-(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)-\d{2}$'
        return bool(re.match(pattern, date))
    
    def check_team_validity(team):
        ssl._create_default_https_context = ssl._create_unverified_context
        teams = (pd.read_html("https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Baseball/Team_abbreviations")[0][0]).tolist()[1:]
        return team in teams
    
    if check_date_format(date):
        if check_team_validity(team):
            data = Game(date, team)
            data.get_pbp()
            data.home_away()
            data.get_pitching_data()
            #data.get_pitching_changes()
            data.get_result()
            
            print(data.Result)
            print(data.innings_scored)
            #print(data.pitching_changes)
            print(data.home_pitchers)
            print(data.away_pitchers)
        else:
            print("Please change team input to format 'MLB'")
    else:
        print("Please change date input to format 'yyyy-MMM-dd'")

print_data()





        
    
    


# data has statistics of every at bat

#####

# Get major statistics from pbp_data for the game
    # Homeruns, Hits, strikeouts

#####

##Need to retrieve the team names from the three letter acronyms