from flask import request
import requests


class Game:
    # constructor
    def __init__(self, game_date, team_abbreviation):
        self.home_pitchers = None
        self.away_pitchers = None
        self.winning_pitcher = None
        self.losing_pitcher = None
        self.teams = None
        self.game = None
        self.pbp = None
        self.game_date = game_date
        self.team_abbreviation = team_abbreviation
        self.standings = None
        self.starting_pitchers = None
        self.innings_scored = None
        self.scoring_plays = {}
        self.pitching_changes = None
        self.Result = None
        self.strikeouts = None
        self.homeTeamHits = None
        self.awayTeamHits = None
        self.homePlayersBatting = {}
        self.awayPlayersBatting = {}
        self.homeTeamHitsByInning = {}
        self.awayTeamHitsByInning = {}
        self.homeRBIs = {}
        self.awayRBIs = {}
        self.topBatters = {}
        # can get 'Last Play', 'Result' (HR/double/ground out/fly out) with paid version of API
        self.BASE_URL = "https://api.sportsdata.io"
        self.API_KEY = "5dfb1139e28a480d9e3f84f84f340c2b"

    def get_team_name(self, abbreviation):
        request_url = f"{self.BASE_URL}/v3/mlb/scores/json/AllTeams?key={self.API_KEY}"
        response = requests.get(request_url)
        if response.status_code == 200:
            team_data = response.json()
            for team in team_data:
                if (team['Active'] == True):
                    if (team['Key'] == abbreviation):
                        return (team['City'] + ' ' + team['Name'])

    def convert_date(self, date):
        month_map = {"JAN": "01",
                     "FEB": "02",
                     "MAR": "03",
                     "APR": "04",
                     "MAY": "05",
                     "JUN": "06",
                     "JUL": "07",
                     "AUG": "08",
                     "SEP": "09",
                     "OCT": "10",
                     "NOV": "11",
                     "DEC": "12"}
        year, month_name, day = date.split("-")
        month_number = month_map[month_name.upper()]
        new_date_str = f"{year}-{month_number}-{day}"
        return new_date_str

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

    def get_team_name(self, abbreviation):
        request_url = f"{self.BASE_URL}/v3/mlb/scores/json/AllTeams?key={self.API_KEY}"
        response = requests.get(request_url)
        if response.status_code == 200:
            team_data = response.json()
            for team in team_data:
                if (team['Active'] == True):
                    if (team['Key'] == abbreviation):
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
        game_id = -1

        for i in range(len(games_data)):
            if games_data[i]['Game']['HomeTeam'] == self.team_abbreviation or games_data[i]['Game']['AwayTeam'] == self.team_abbreviation:
                desired_game_index = i
                game_id = games_data[i]['Game']['GameID']
                break
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
            # print("successful response")
            pbp_data = response2.json()
            self.pbp = pbp_data['Plays']
            self.game = pbp_data['Game']

    def home_away(self):
        home = self.game['HomeTeam']
        away = self.game['AwayTeam']
        self.teams = {'Home': self.get_team_name(
            home), 'Away': self.get_team_name(away)}

    def get_result(self):
        homeTotalRuns = 0
        homeInningsScored = {}
        awayTotalRuns = 0
        awayInningsScored = {}
        innings_data = self.game['Innings']
        for inning in innings_data:
            if inning['HomeTeamRuns'] is not None and inning['HomeTeamRuns'] > 0:
                homeTotalRuns += inning['HomeTeamRuns']
                homeInningsScored[inning['InningNumber']
                                  ] = inning['HomeTeamRuns']
            if inning['AwayTeamRuns'] is not None and inning['AwayTeamRuns'] > 0:
                awayTotalRuns += inning['AwayTeamRuns']
                awayInningsScored[inning['InningNumber']
                                  ] = inning['AwayTeamRuns']
        self.Result = {'Home': homeTotalRuns, 'Away': awayTotalRuns}
        self.innings_scored = {
            'Home': homeInningsScored, 'Away': awayInningsScored}

    def get_batting_data(self):
        awayTeamHits = 0
        homeTeamHits = 0
        awayHitsByInning = {}
        awayPlayerHits = {}
        homeHitsByInning = {}
        homePlayerHits = {}
        for play in self.pbp:
            if play['InningHalf'] == 'T':  # away team batting
                if play['HitterName'] not in awayPlayerHits.keys():
                    awayPlayerHits[play['HitterName']] = 0
                if play['Hit'] == True:
                    awayTeamHits += 1
                    if play['InningNumber'] in awayHitsByInning.keys():
                        awayHitsByInning[play['InningNumber']] += 1
                    else:
                        awayHitsByInning[play['InningNumber']] = 1
                    awayPlayerHits[play['HitterName']] += 1
            elif play['InningHalf'] == 'B':  # home team batting
                if play['HitterName'] not in homePlayerHits.keys():
                    homePlayerHits[play['HitterName']] = 0
                if play['Hit'] == True:
                    homeTeamHits += 1
                    if play['InningNumber'] in homeHitsByInning.keys():
                        homeHitsByInning[play['InningNumber']] += 1
                    else:
                        homeHitsByInning[play['InningNumber']] = 1
                    homePlayerHits[play['HitterName']] += 1
            self.homeTeamHits = homeTeamHits
            self.awayTeamHits = awayTeamHits
            self.homePlayersBatting = homePlayerHits
            self.awayPlayersBatting = awayPlayerHits
            self.homeTeamHitsByInning = homeHitsByInning
            self.awayTeamHitsByInning = awayHitsByInning

    def combine_batter_stats(self, hits, rbis):
        combined_stats = {}

        for player, hit_count in hits.items():
            if player not in combined_stats:
                combined_stats[player] = {'hits': 0, 'RBIs': 0}
            combined_stats[player]['hits'] = hit_count

        for inning, rbi_list in rbis.items():
            for rbi_data in rbi_list:
                player, rbi_count = rbi_data
                if player not in combined_stats:
                    combined_stats[player] = {'hits': 0, 'RBIs': 0}
                combined_stats[player]['RBIs'] += rbi_count

        # Remove players with 0 hits and 0 RBIs
        combined_stats = {player: stats for player, stats in combined_stats.items(
        ) if stats['hits'] > 0 or stats['RBIs'] > 0}

        return combined_stats

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
            if (play['InningHalf'] == 'B'):
                if (currentPitcher not in away_ids.keys()):
                    away_ids[currentPitcher] = 1
                else:
                    away_ids[currentPitcher] += 1
            if (play['InningHalf'] == 'T'):
                if (currentPitcher not in home_ids.keys()):
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
            if (play['InningHalf'] == 'B'):
                if (play['PitcherID'] != awayid):
                    changes.append({'Inning': play['InningNumber'], 'Play': play['PlayNumber'],
                                    'Team': self.game['AwayTeam'], 'Old': self.get_player_name(awayid),
                                    'New': self.get_player_name(play['PitcherID'])})
                    awayid = play['PitcherID']
            else:
                if (play['PitcherID'] != homeid):
                    changes.append({'Inning': play['InningNumber'], 'Play': play['PlayNumber'],
                                    'Team': self.game['HomeTeam'], 'Old': self.get_player_name(homeid),
                                    'New': self.get_player_name(play['PitcherID'])})
                    homeid = play['PitcherID']
        self.pitching_changes = changes

    def get_scoring_plays(self):
        for play in self.pbp:
            currentInning = play['InningNumber']
            if play['InningHalf'] == 'T':  # away team bats first
                if currentInning not in self.awayRBIs.keys():
                    self.awayRBIs[currentInning] = []
                if play['RunsBattedIn'] > 0:
                    self.awayRBIs[currentInning].append(
                        (play['HitterName'], play['RunsBattedIn']))
            else:
                if currentInning not in self.homeRBIs.keys():
                    self.homeRBIs[currentInning] = []
                if play['RunsBattedIn'] > 0:
                    self.homeRBIs[currentInning].append(
                        (play['HitterName'], play['RunsBattedIn']))

    def get_wl_pitchers(self):
        winning_pitcherID = self.game['WinningPitcherID']
        losing_pitcherID = self.game['LosingPitcherID']
        if self.game['HomeTeamRuns'] > self.game['AwayTeamRuns']:
            self.winning_pitcher = (self.get_player_name(
                winning_pitcherID), self.game['HomeTeam'])
            self.losing_pitcher = (self.get_player_name(
                losing_pitcherID), self.game['AwayTeam'])
        else:
            self.winning_pitcher = (self.get_player_name(
                winning_pitcherID), self.game['AwayTeam'])
            self.losing_pitcher = (self.get_player_name(
                losing_pitcherID), self.game['HomeTeam'])


def get_game_prompt(date, team):
    def create_prompt(Game):
        home_team_innings_scored = Game.innings_scored['Home']
        away_team_innings_scored = Game.innings_scored['Away']
        homeTeamTopBatters = Game.combine_batter_stats(
            Game.homePlayersBatting, Game.homeRBIs)
        awayTeamTopBatters = Game.combine_batter_stats(
            Game.awayPlayersBatting, Game.awayRBIs)

        home_innings = ', '.join(
            f"{inning}: {score}" for inning, score in home_team_innings_scored.items())
        away_innings = ', '.join(
            f"{inning}: {score}" for inning, score in away_team_innings_scored.items())
        home_hits_by_inning = ', '.join(
            f"{inning}: {hits}" for inning, hits in Game.homeTeamHitsByInning.items())
        away_hits_by_inning = ', '.join(
            f"{inning}: {hits}" for inning, hits in Game.awayTeamHitsByInning.items())
        home_pitchers = ', '.join(Game.home_pitchers.keys())
        away_pitchers = ', '.join(Game.away_pitchers.keys())
        home_batters = ', '.join(
            f"{name}: {stats}" for name, stats in homeTeamTopBatters.items())
        away_batters = ', '.join(
            f"{name}: {stats}" for name, stats in awayTeamTopBatters.items())

        prompt = f"Generate a summary story for an MLB game with the following key stats and events:\n\
            Home Team ({Game.teams['Home']}):\n\
                - Innings Scored: {home_innings}\n\
                - Total Hits: {Game.homeTeamHits}\n\
                - Hits by Inning: {home_hits_by_inning}\n\
                - Pitchers: {home_pitchers}\n\
                - Top Batters: {home_batters}\n\
            Away Team ({Game.teams['Away']}):\n\
                - Innings Scored: {away_innings}\n\
                - Total Hits: {Game.awayTeamHits}\n\
                - Hits by Inning: {away_hits_by_inning}\n\
                - Pitchers: {away_pitchers}\n\
                - Top Batters: {away_batters}"
        return prompt

    # data = Game('2023-MAY-13', 'LAD')
    data = Game(date, team)
    data.get_pbp()
    data.home_away()
    data.get_pitching_data()
    data.get_result()
    data.get_batting_data()
    data.get_scoring_plays()
    data.get_wl_pitchers()
    game_prompt = create_prompt(data)
    messages = [
        {"role": "system", "content": "You are an AI designed to input formatted stats from a baseball game and return a narrative story about what happened in the game"},
        {"role": "user", "content": game_prompt}
    ]

    res = {"data": messages}

    return res
