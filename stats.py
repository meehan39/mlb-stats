import statsapi
import string
from static import *

def get_teams():
    team_codes = []
    for team in teams:
        team_codes.append(team)
    return team_codes

def get_roster(team_code):
    team_data = {
        'team_name': team_names[team_code],
        'team_code': team_code,
        'roster': []
    }
    roster = rosters[team_code]
    for player in roster:
        home_runs = 0
        player_name = player
        if player in player_ids:
            player_data = []
            player_id = player_ids[player]
            stats = statsapi.player_stat_data(player_id, 'hitting', 'season')
            home_runs = stats["stats"][0]["stats"]["homeRuns"]

        else:
            player_data = statsapi.lookup_player(player)
            if (len(player_data) > 0):
                player_id = player_data[0]["id"]
                player_name = player_data[0]["fullName"]
                stats = statsapi.player_stat_data(player_id, 'hitting', 'season')
                home_runs = stats["stats"][0]["stats"]["homeRuns"]

        team_data["roster"].append({
            "player_name": string.capwords(player_name),
            "home_runs": home_runs
        })
    return team_data

def get_total_homeruns(team_data):
    total = 0
    for player_data in team_data["roster"]:
        total += player_data["home_runs"]
    return total

def sort_standings_func(team_data):
    return team_data["home_runs"]

def get_player_ids():
    ids = {}
    for team_name in teams:
        for player_name in teams[team_name]:
            player_data = statsapi.lookup_player(player_name)
            if (len(player_data) > 0):
                ids[player_name.lower()] = player_data[0]["id"]
    print(ids)
    player_ids = ids

