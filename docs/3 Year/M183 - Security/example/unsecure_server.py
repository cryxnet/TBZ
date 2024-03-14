from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/follow')
def follow_url():
    url = request.args.get('url', '')
    if url:
        return requests.get(url).text
    return "no url parameter provided"

@app.route('/login')
def login():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login Page</title>
    </head>
    <body>
        <h1>Login Page</h1>
        <form action="/follow?url=http://" method="get">
            <input type="hidden" name="url" value="/">
            <button type="submit">Go to Home Page</button>
        </form>
    </body>
    </html>
    """

@app.route('/')
def home():
    return "Home Page"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
