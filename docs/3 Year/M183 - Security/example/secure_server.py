from flask import Flask, request, abort
import requests

app = Flask(__name__)

# Erlaubte Hosts definieren
ALLOWED_HOSTS = ['10.62.104.244']

def is_allowed_url(url):
    """Überprüfen, ob die URL zu einem erlaubten Host gehört."""
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    return parsed_url.netloc in ALLOWED_HOSTS

@app.route('/follow')
def follow_url():
    url = request.args.get('url', '')
    if url:
        # Überprüfen, ob die URL erlaubt ist
        if not is_allowed_url(url):
            return "Diese URL ist nicht erlaubt.", 403

        # Anfragen mit Timeout, um Blockierungen zu vermeiden
        try:
            response = requests.get(url, timeout=5)
            return response.text
        except requests.RequestException as e:
            # Einfache Fehlerbehandlung
            return f"Ein Fehler ist aufgetreten: {e}", 500

    return "Kein URL-Parameter angegeben"

@app.route('/login')
def follow_url():
    return "Login Page"