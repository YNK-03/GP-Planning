import requests
from flask import Flask, render_template_string

app = Flask(__name__)

# ==========================================
# FORMULE 1 (Ergast API pour 2025 - gratuit)
# ==========================================
F1_CALENDAR_URL = "http://ergast.com/api/f1/2025.json"
F1_STANDINGS_URL = "http://ergast.com/api/f1/2025/driverStandings.json"

def get_f1_calendar():
    """Récupère le calendrier F1 pour 2025 via l'Ergast API."""
    try:
        response = requests.get(F1_CALENDAR_URL)
        data = response.json()
        calendar = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])
        return calendar
    except Exception as e:
        print("Erreur lors de la récupération du calendrier F1:", e)
        return []

def get_f1_standings():
    """Récupère le classement des pilotes F1 pour 2025 via l'Ergast API."""
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


# ==========================================
# MOTO GP (exemple avec API - version 2025)
# ==========================================
# Remplacez "YOUR_MOTOGP_API_KEY" par votre clé API réelle
MOTO_GP_API_KEY = "YOUR_MOTOGP_API_KEY"
MOTO_GP_CALENDAR_URL = f"https://api.sportradar.us/motogp/trial/v2/en/schedule/2025.json?api_key={MOTO_GP_API_KEY}"
MOTO_GP_STANDINGS_URL = f"https://api.sportradar.us/motogp/trial/v2/en/standings/2025.json?api_key={MOTO_GP_API_KEY}"

def get_motogp_calendar():
    """Récupère le calendrier MotoGP pour 2025 via l'API choisie."""
    try:
        response = requests.get(MOTO_GP_CALENDAR_URL)
        data = response.json()
        # La clé 'schedule' doit être adaptée selon la structure renvoyée par l'API
        calendar = data.get('schedule', [])
        return calendar
    except Exception as e:
        print("Erreur lors de la récupération du calendrier MotoGP:", e)
        return []

def get_motogp_standings():
    """Récupère le classement MotoGP pour 2025 via l'API choisie."""
    try:
        response = requests.get(MOTO_GP_STANDINGS_URL)
        data = response.json()
        # Ajustez l'extraction en fonction de la réponse de l'API
        standings = data.get('standings', [])
        return standings
    except Exception as e:
        print("Erreur lors de la récupération du classement MotoGP:", e)
        return []


# ==========================================
# WSBK (exemple avec API - version 2025)
# ==========================================
# Remplacez "YOUR_WSBK_API_KEY" par votre clé API réelle
WSBK_API_KEY = "YOUR_WSBK_API_KEY"
WSBK_CALENDAR_URL = f"https://api.sportradar.us/wsbk/trial/v2/en/schedule/2025.json?api_key={WSBK_API_KEY}"
WSBK_STANDINGS_URL = f"https://api.sportradar.us/wsbk/trial/v2/en/standings/2025.json?api_key={WSBK_API_KEY}"

def get_wsbk_calendar():
    """Récupère le calendrier WSBK pour 2025 via l'API choisie."""
    try:
        response = requests.get(WSBK_CALENDAR_URL)
        data = response.json()
        calendar = data.get('schedule', [])
        return calendar
    except Exception as e:
        print("Erreur lors de la récupération du calendrier WSBK:", e)
        return []

def get_wsbk_standings():
    """Récupère le classement WSBK pour 2025 via l'API choisie."""
    try:
        response = requests.get(WSBK_STANDINGS_URL)
        data = response.json()
        standings = data.get('standings', [])
        return standings
    except Exception as e:
        print("Erreur lors de la récupération du classement WSBK:", e)
        return []


# ==========================================
# GT3 (exemple avec API - version 2025)
# ==========================================
# Remplacez "YOUR_GT3_API_KEY" par votre clé API réelle
GT3_API_KEY = "YOUR_GT3_API_KEY"
GT3_CALENDAR_URL = f"https://api.sportradar.us/gt3/trial/v2/en/schedule/2025.json?api_key={GT3_API_KEY}"
GT3_STANDINGS_URL = f"https://api.sportradar.us/gt3/trial/v2/en/standings/2025.json?api_key={GT3_API_KEY}"

def get_gt3_calendar():
    """Récupère le calendrier GT3 pour 2025 via l'API choisie."""
    try:
        response = requests.get(GT3_CALENDAR_URL)
        data = response.json()
        calendar = data.get('schedule', [])
        return calendar
    except Exception as e:
        print("Erreur lors de la récupération du calendrier GT3:", e)
        return []

def get_gt3_standings():
    """Récupère le classement GT3 pour 2025 via l'API choisie."""
    try:
        response = requests.get(GT3_STANDINGS_URL)
        data = response.json()
        standings = data.get('standings', [])
        return standings
    except Exception as e:
        print("Erreur lors de la récupération du classement GT3:", e)
        return []


# ==========================================
# Style CSS moderne et épuré
# ==========================================
css_style = """
    body { margin:0; padding:0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background-color: #f4f4f4; color: #333; }
    .container { width: 80%; margin: 0 auto; padding: 20px; }
    header { background: #333; color: #fff; padding: 10px 20px; text-align: center; }
    nav a { color: #fff; margin: 0 10px; text-decoration: none; }
    nav a:hover { text-decoration: underline; }
    main { padding: 20px 0; }
    h1, h2 { color: #444; }
    ul, ol { list-style: none; padding: 0; }
    li { background: #fff; margin-bottom: 10px; padding: 10px; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    a { color: #1d70b8; text-decoration: none; }
    a:hover { text-decoration: underline; }
    footer { text-align: center; padding: 20px; margin-top: 20px; color: #777; }
"""

# ==========================================
# Routes de l'application Flask
# ==========================================
@app.route('/')
def index():
    html = (
        "<!doctype html>"
        "<html lang='fr'>"
        "<head>"
        "    <meta charset='UTF-8'>"
        "    <title>Racing Info</title>"
        "    <style>" + css_style + "</style>"
        "</head>"
        "<body>"
        "  <div class='container'>"
        "     <header>"
        "       <h1>Racing Info</h1>"
        "       <nav>"
        "         <a href='/'>Accueil</a>"
        "         <a href='/f1'>Formule 1</a>"
        "         <a href='/motogp'>MotoGP</a>"
        "         <a href='/wsbk'>WSBK</a>"
        "         <a href='/gt3'>GT3</a>"
        "       </nav>"
        "     </header>"
        "     <main>"
        "       <h2>Bienvenue sur l'application Racing Info</h2>"
        "       <ul>"
        "         <li><a href='/f1'>Formule 1</a></li>"
        "         <li><a href='/motogp'>MotoGP</a></li>"
        "         <li><a href='/wsbk'>WSBK</a></li>"
        "         <li><a href='/gt3'>GT3</a></li>"
        "       </ul>"
        "     </main>"
        "     <footer>"
        "       <p>© 2025 Racing Info</p>"
        "     </footer>"
        "  </div>"
        "</body>"
        "</html>"
    )
    return render_template_string(html)

@app.route('/f1')
def f1():
    calendar = get_f1_calendar()
    standings = get_f1_standings()
    html = (
        "<!doctype html>"
        "<html lang='fr'>"
        "<head>"
        "    <meta charset='UTF-8'>"
        "    <title>Calendrier et Standings F1</title>"
        "    <style>" + css_style + "</style>"
        "</head>"
        "<body>"
        "  <div class='container'>"
        "     <header>"
        "       <h1>Formule 1</h1>"
        "       <nav>"
        "         <a href='/'>Accueil</a>"
        "         <a href='/f1'>F1</a>"
        "         <a href='/motogp'>MotoGP</a>"
        "         <a href='/wsbk'>WSBK</a>"
        "         <a href='/gt3'>GT3</a>"
        "       </nav>"
        "     </header>"
        "     <main>"
        "       <section>"
        "          <h2>Calendrier Formule 1</h2>"
        "          <ul>"
        "          {% for race in calendar %}"
        "             <li>"
        "               <strong>{{ race['raceName'] }}</strong> à {{ race['Circuit']['circuitName'] }} le {{ race['date'] }}"
        "             </li>"
        "          {% endfor %}"
        "          </ul>"
        "       </section>"
        "       <section>"
        "          <h2>Classement des pilotes</h2>"
        "          <ol>"
        "          {% for driver in standings %}"
        "             <li>"
        "               {{ driver['Driver']['givenName'] }} {{ driver['Driver']['familyName'] }} - {{ driver['points'] }} pts"
        "             </li>"
        "          {% endfor %}"
        "          </ol>"
        "       </section>"
        "       <a href='/'>Retour</a>"
        "     </main>"
        "     <footer>"
        "       <p>© 2025 Racing Info</p>"
        "     </footer>"
        "  </div>"
        "</body>"
        "</html>"
    )
    return render_template_string(html, calendar=calendar, standings=standings)

@app.route('/motogp')
def motogp():
    calendar = get_motogp_calendar()
    standings = get_motogp_standings()
    html = (
        "<!doctype html>"
        "<html lang='fr'>"
        "<head>"
        "    <meta charset='UTF-8'>"
        "    <title>Calendrier et Standings MotoGP</title>"
        "    <style>" + css_style + "</style>"
        "</head>"
        "<body>"
        "  <div class='container'>"
        "     <header>"
        "       <h1>MotoGP</h1>"
        "       <nav>"
        "         <a href='/'>Accueil</a>"
        "         <a href='/f1'>F1</a>"
        "         <a href='/motogp'>MotoGP</a>"
        "         <a href='/wsbk'>WSBK</a>"
        "         <a href='/gt3'>GT3</a>"
        "       </nav>"
        "     </header>"
        "     <main>"
        "       <section>"
        "          <h2>Calendrier MotoGP</h2>"
        "          <ul>"
        "          {% for race in calendar %}"
        "             <li>"
        "               <strong>{{ race.get('raceName', 'Course inconnue') }}</strong> à {{ race.get('location', 'Lieu inconnu') }} le {{ race.get('date', 'Date inconnue') }}"
        "             </li>"
        "          {% endfor %}"
        "          </ul>"
        "       </section>"
        "       <section>"
        "          <h2>Classement</h2>"
        "          <ol>"
        "          {% for entry in standings %}"
        "             <li>{{ entry.get('driver', 'Pilote inconnu') }} - {{ entry.get('points', '0') }} pts</li>"
        "          {% endfor %}"
        "          </ol>"
        "       </section>"
        "       <a href='/'>Retour</a>"
        "     </main>"
        "     <footer>"
        "       <p>© 2025 Racing Info</p>"
        "     </footer>"
        "  </div>"
        "</body>"
        "</html>"
    )
    return render_template_string(html, calendar=calendar, standings=standings)

@app.route('/wsbk')
def wsbk():
    calendar = get_wsbk_calendar()
    standings = get_wsbk_standings()
    html = (
        "<!doctype html>"
        "<html lang='fr'>"
        "<head>"
        "    <meta charset='UTF-8'>"
        "    <title>Calendrier et Standings WSBK</title>"
        "    <style>" + css_style + "</style>"
        "</head>"
        "<body>"
        "  <div class='container'>"
        "     <header>"
        "       <h1>WSBK</h1>"
        "       <nav>"
        "         <a href='/'>Accueil</a>"
        "         <a href='/f1'>F1</a>"
        "         <a href='/motogp'>MotoGP</a>"
        "         <a href='/wsbk'>WSBK</a>"
        "         <a href='/gt3'>GT3</a>"
        "       </nav>"
        "     </header>"
        "     <main>"
        "       <section>"
        "          <h2>Calendrier WSBK</h2>"
        "          <ul>"
        "          {% for race in calendar %}"
        "             <li>"
        "               <strong>{{ race.get('raceName', 'Course inconnue') }}</strong> à {{ race.get('location', 'Lieu inconnu') }} le {{ race.get('date', 'Date inconnue') }}"
        "             </li>"
        "          {% endfor %}"
        "          </ul>"
        "       </section>"
        "       <section>"
        "          <h2>Classement</h2>"
        "          <ol>"
        "          {% for entry in standings %}"
        "             <li>{{ entry.get('rider', 'Pilote inconnu') }} - {{ entry.get('points', '0') }} pts</li>"
        "          {% endfor %}"
        "          </ol>"
        "       </section>"
        "       <a href='/'>Retour</a>"
        "     </main>"
        "     <footer>"
        "       <p>© 2025 Racing Info</p>"
        "     </footer>"
        "  </div>"
        "</body>"
        "</html>"
    )
    return render_template_string(html, calendar=calendar, standings=standings)

@app.route('/gt3')
def gt3():
    calendar = get_gt3_calendar()
    standings = get_gt3_standings()
    html = (
        "<!doctype html>"
        "<html lang='fr'>"
        "<head>"
        "    <meta charset='UTF-8'>"
        "    <title>Calendrier et Standings GT3</title>"
        "    <style>" + css_style + "</style>"
        "</head>"
        "<body>"
        "  <div class='container'>"
        "     <header>"
        "       <h1>GT3</h1>"
        "       <nav>"
        "         <a href='/'>Accueil</a>"
        "         <a href='/f1'>F1</a>"
        "         <a href='/motogp'>MotoGP</a>"
        "         <a href='/wsbk'>WSBK</a>"
        "         <a href='/gt3'>GT3</a>"
        "       </nav>"
        "     </header>"
        "     <main>"
        "       <section>"
        "          <h2>Calendrier GT3</h2>"
        "          <ul>"
        "          {% for race in calendar %}"
        "             <li>"
        "               <strong>{{ race.get('raceName', 'Événement inconnu') }}</strong> à {{ race.get('location', 'Lieu inconnu') }} le {{ race.get('date', 'Date inconnue') }}"
        "             </li>"
        "          {% endfor %}"
        "          </ul>"
        "       </section>"
        "       <section>"
        "          <h2>Classement</h2>"
        "          <ol>"
        "          {% for entry in standings %}"
        "             <li>{{ entry.get('team', 'Équipe inconnue') }} - {{ entry.get('points', '0') }} pts</li>"
        "          {% endfor %}"
        "          </ol>"
        "       </section>"
        "       <a href='/'>Retour</a>"
        "     </main>"
        "     <footer>"
        "       <p>© 2025 Racing Info</p>"
        "     </footer>"
        "  </div>"
        "</body>"
        "</html>"
    )
    return render_template_string(html, calendar=calendar, standings=standings)

if __name__ == '__main__':
    app.run(debug=True)
