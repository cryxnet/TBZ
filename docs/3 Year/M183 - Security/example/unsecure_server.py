from flask import *
import requests

app = Flask(__name__)

@app.route('/follow')
def follow_url():
    url = request.args.get('url', '')
    if url:
        return (requests.get(url).text)

    return "no url parameter provided"

@app.route('/login')
def follow_url():
    return "Login Page"

app.run(host='0.0.0.0', port=8888)