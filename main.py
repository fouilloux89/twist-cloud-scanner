from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Page d'accueil</h2><p><a href='/scan'>Tester /scan</a></p>"

@app.route("/scan")
def scan_all():
    print("✅ La route /scan est bien appelée !")
    return "✅ Ceci est la réponse de /scan."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
