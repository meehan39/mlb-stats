from flask import (Flask, g, render_template, request)
from .stats import *


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def home():
        rosters = []
        g.standings = []
        for team in team_names:
            roster = get_roster(team)
            rosters.append(roster)
            g.standings.append({
                "team_code": team,
                "team_name": roster["team_name"],
                "home_runs": get_total_homeruns(roster)
            })
            g.standings.sort(key=sort_standings_func, reverse=True)
        return render_template('index.html')
        # return g.standings

    @app.route('/team')
    def team():
        team_code = request.args.get('code')
        g.team_code = team_code
        g.team_name = team_names[team_code]
        g.roster = get_roster(team_code)['roster']
        return render_template('team.html')
        

    return app