from flask import Flask
from tvDatafeed import TvDatafeed, Interval
import pandas_ta as ta

app = Flask(__name__)
tv = TvDatafeed()  # ← ajoute tes identifiants si nécessaire

# 🔍 Symboles à scanner
symbols = [
    ('MGC1!', 'COMEX'),
    ('MNQ1!', 'CME'),
    ('MYM1!', 'CBOT'),
    ('M6E1!', 'CME'),
    ('MBT1!', 'CME'),
    ('MCL1!', 'NYMEX'),
    ('MES1!', 'CME'),
    ('ES1!', 'CME'),
    ('YM1!', 'CBOT'),
]

# ⏱️ Timeframes à utiliser
timeframes = {
    '1h': Interval.in_1_hour,
    '1d': Interval.in_daily
}

# 📊 Détection du twist Ichimoku
def detect_twist(df):
    ichimoku = ta.ichimoku(df['high'], df['low'])[0]
    spanA = ichimoku['ISA_9']
    spanB = ichimoku['ISB_26']
    for i in range(len(spanA) - 10, len(spanA)):
        if (spanA[i] > spanB[i] and spanA[i-1] < spanB[i-1]) or \
           (spanA[i] < spanB[i] and spanA[i-1] > spanB[i-1]):
            return True
    return False

# 🌐 Page d'accueil
@app.route("/")
def home():
    return "<h2>Accueil TwistBot</h2><p><a href='/scan'>📊 Lancer le scan</a></p>"

# 🚀 Route de scan
@app.route("/scan")
def scan():
    results = []
    for sym, exch in symbols:
        for tf_name, tf in timeframes.items():
            try:
                df = tv.get_hist(sym, exchange=exch, interval=tf, n_bars=200)
                if df is not None and detect_twist(df):
                    results.append(f"🌀 Twist détecté sur {sym} ({exch}) en {tf_name}")
            except Exception as e:
                results.append(f"⚠️ Erreur sur {sym} ({tf_name}) : {e}")
    if not results:
        return "✅ Aucun twist détecté."
    return "<br>".join(results)

# 🚦 Lancer le serveur
if __name__ == "__main__":
    app.run()
