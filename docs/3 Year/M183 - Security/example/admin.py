from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def main():
   return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Admin Dashboard</title>
        </head>
        <body>
            <h1>Admin Dashboard</h1>
            <p>Dieses Dashboard ist nur aus dem internen Netzwerk zugänglich.</p>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='9999')
