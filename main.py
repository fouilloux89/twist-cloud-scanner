from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Twist Scanner en ligne 🚀</h2><p><a href='/scan'>Lancer le scan</a></p>"

@app.route("/scan")
def scan_all():
    print("🧪 La route /scan est appelée !")
    return "✅ Scan simulé avec succès !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

