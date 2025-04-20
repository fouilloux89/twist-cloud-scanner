from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Accueil"

@app.route("/scan")
def scan():
    return "Scan OK"

if __name__ == "__main__":
    app.run(port=5000)
