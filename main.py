from flask import Flask
import os

# Supposons que tu as une fonction dans un autre fichier
from twist_utils import scanner  

app = Flask(__name__)

@app.route('/')
def hello():
    return "Twist Scanner en ligne 🚀"

@app.route('/scan')
def lancer_scan():
    resultat = scanner()
    return f"Résultat du scan : {resultat}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
