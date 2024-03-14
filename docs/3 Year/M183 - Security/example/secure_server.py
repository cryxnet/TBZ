from flask import Flask, request, abort
import requests
from urllib.parse import urlparse

app = Flask(__name__)

# Erlaubte Hosts definieren
ALLOWED_HOSTS = ['10.62.104.222:8881']

def is_valid_url(url):
    """Überprüfen, ob die URL gültig und zu einem erlaubten Host gehört."""
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc in ALLOWED_HOSTS

def is_safe_redirect(target):
    """Überprüfen, ob die Weiterleitung sicher ist (keine Umleitung auf interne Ressourcen)."""
    return urlparse(request.host_url).netloc == urlparse(target).netloc

@app.route('/follow')
def follow_url():
    url = request.args.get('url', '')
    if url:
        # Überprüfen, ob die URL gültig und erlaubt ist
        if not is_valid_url(url):
            return "Diese URL ist nicht erlaubt.", 403

        # Überprüfen, ob die Weiterleitung sicher ist
        if not is_safe_redirect(url):
            return "Unsichere Weiterleitung.", 403

        # Anfragen mit Timeout, um Blockierungen zu vermeiden
        try:
            response = requests.get(url, timeout=5)
            return response.text
        except requests.RequestException as e:
            # Einfache Fehlerbehandlung
            return f"Ein Fehler ist aufgetreten: {e}", 500

    return "Kein URL-Parameter angegeben"

@app.route('/login')
def login_page():
    return "Login Page"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8881)
