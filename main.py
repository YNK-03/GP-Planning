import requests
from flask import Flask, render_template_string

app = Flask(__name__)

# -----------------------
# Fonctions pour Formule 1
# -----------------------
F1_CALENDAR_URL = "http://ergast.com/api/f1/current.json"
F1_STANDINGS_URL = "http://ergast.com/api/f1/current/driverStandings.json"

def get_f1_calendar():
    """Récupère le calendrier F1 via l'API Ergast."""
    try:
        response = requests.get(F1_CALENDAR_URL)
        data = response.json()
        # Extraction de la liste des courses
        calendar = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])
        return calendar
    except Exception as e:
        print("Erreur lors de la récupération du calendrier F1:", e)
        return []

def get_f1_standings():
    """Récupère le classement des pilotes F1 via l'API Ergast."""
    try:
        response = requests.get(F1_STANDINGS_URL)
        data = response.json()
        standings_list = data.get('MRData', {}).get('StandingsTable', {}).get('StandingsLists', [])
        if standings_list:
            return standings_list[0].get('DriverStandings', [])
        else:
            return []
    except Exception as e:
        print("Erreur lors de la récupération du classement F1:", e)
        return []

# ---------------------------
# Fonctions pour MotoGP (exemple)
# ---------------------------
def get_motogp_calendar():
    """
    Placeholder pour le calendrier MotoGP.
    À remplacer par une récupération des données via une API ou du web scraping.
    """
    return [
        {"raceName": "MotoGP Example Grand Prix", "date": "2024-05-01", "location": "Circuit Example"}
    ]

def get_motogp_standings():
    """Placeholder pour le classement MotoGP."""
    return [
        {"position": 1, "driver": "Pilote A", "points": 150},
        {"position": 2, "driver": "Pilote B", "points": 140},
    ]

# ---------------------------
# Fonctions pour WSBK (exemple)
# ---------------------------
def get_wsbk_calendar():
    """Placeholder pour le calendrier WSBK."""
    return [
        {"raceName": "WSBK Example Round", "date": "2024-06-15", "location": "Circuit WSBK"}
    ]

def get_wsbk_standings():
    """Placeholder pour le classement WSBK."""
    return [
        {"position": 1, "rider": "Rider X", "points": 130},
        {"position": 2, "rider": "Rider Y", "points": 120},
    ]

# ---------------------------
# Fonctions pour GT3 (exemple)
# ---------------------------
def get_gt3_calendar():
    """Placeholder pour le calendrier GT3."""
    return [
        {"raceName": "GT3 Example Event", "date": "2024-07-20", "location": "Circuit GT3"}
    ]

def get_gt3_standings():
    """Placeholder pour le classement GT3."""
    return [
        {"position": 1, "team": "Team 1", "points": 110},
        {"position": 2, "team": "Team 2", "points": 100},
    ]

# ---------------------------
# Routes de l'application Flask
# ---------------------------
@app.route('/')
def index():
    html = """
    <h1>Bienvenue sur l'application Racing Info</h1>
    <ul>
        <li><a href="/f1">Formule 1</a></li>
        <li><a href="/motogp">MotoGP</a></li>
        <li><a href="/wsbk">WSBK</a></li>
        <li><a href="/gt3">GT3</a></li>
    </ul>
    """
    return render_template_string(html)

@app.route('/f1')
def f1():
    calendar = get_f1_calendar()
    standings = get_f1_standings()
    html = """
    <h1>Calendrier Formule 1</h1>
    <ul>
    {% for race in calendar %}
       <li>
         <strong>{{ race['raceName'] }}</strong> à {{ race['Circuit']['circuitName'] }} le {{ race['date'] }}
       </li>
    {% endfor %}
    </ul>

    <h2>Classement des pilotes</h2>
    <ol>
    {% for driver in standings %}
       <li>
         {{ driver['Driver']['givenName'] }} {{ driver['Driver']['familyName'] }} - {{ driver['points'] }} pts
       </li>
    {% endfor %}
    </ol>
    <a href="/">Retour</a>
    """
    return render_template_string(html, calendar=calendar, standings=standings)

@app.route('/motogp')
def motogp():
    calendar = get_motogp_calendar()
    standings = get_motogp_standings()
    html = """
    <h1>Calendrier MotoGP (exemple)</h1>
    <ul>
    {% for race in calendar %}
       <li>
         <strong>{{ race['raceName'] }}</strong> à {{ race['location'] }} le {{ race['date'] }}
       </li>
    {% endfor %}
    </ul>

    <h2>Classement</h2>
    <ol>
    {% for entry in standings %}
       <li>{{ entry['driver'] }} - {{ entry['points'] }} pts</li>
    {% endfor %}
    </ol>
    <a href="/">Retour</a>
    """
    return render_template_string(html, calendar=calendar, standings=standings)

@app.route('/wsbk')
def wsbk():
    calendar = get_wsbk_calendar()
    standings = get_wsbk_standings()
    html = """
    <h1>Calendrier WSBK (exemple)</h1>
    <ul>
    {% for race in calendar %}
       <li>
         <strong>{{ race['raceName'] }}</strong> à {{ race['location'] }} le {{ race['date'] }}
       </li>
    {% endfor %}
    </ul>

    <h2>Classement</h2>
    <ol>
    {% for entry in standings %}
       <li>{{ entry['rider'] }} - {{ entry['points'] }} pts</li>
    {% endfor %}
    </ol>
    <a href="/">Retour</a>
    """
    return render_template_string(html, calendar=calendar, standings=standings)

@app.route('/gt3')
def gt3():
    calendar = get_gt3_calendar()
    standings = get_gt3_standings()
    html = """
    <h1>Calendrier GT3 (exemple)</h1>
    <ul>
    {% for race in calendar %}
       <li>
         <strong>{{ race['raceName'] }}</strong> à {{ race['location'] }} le {{ race['date'] }}
       </li>
    {% endfor %}
    </ul>

    <h2>Classement</h2>
    <ol>
    {% for entry in standings %}
       <li>{{ entry['team'] }} - {{ entry['points'] }} pts</li>
    {% endfor %}
    </ol>
    <a href="/">Retour</a>
    """
    return render_template_string(html, calendar=calendar, standings=standings)

# Lancement de l'application
if __name__ == '__main__':
    app.run(debug=True)
