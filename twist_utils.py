from tvDatafeed import TvDatafeed, Interval
import pandas_ta as ta

# Connexion à TradingView
tv = TvDatafeed()  # Peut aussi prendre login/password si besoin

SYMBOLS = ["MNQ1!", "MGC1!", "MYM1!", "M6E1!", "MBT1!", "MCL1!", "MES1!", "ES1!", "YM1!"]
TIMEFRAMES = {
    "1m": Interval.in_1_minute,
    "5m": Interval.in_5_minute,
    "15m": Interval.in_15_minute,
    "1h": Interval.in_1_hour,
    "4h": Interval.in_4_hour
}

def detect_twist(df):
    ichimoku = ta.ichimoku(df['high'], df['low'], df['close'])
    senkou_a = ichimoku['ISA_9']
    senkou_b = ichimoku['ISB_26']
    
    # Vérifie si le twist se produit (croisement)
    if len(senkou_a) < 2 or len(senkou_b) < 2:
        return False
    return (senkou_a.iloc[-2] < senkou_b.iloc[-2] and senkou_a.iloc[-1] > senkou_b.iloc[-1]) or \
           (senkou_a.iloc[-2] > senkou_b.iloc[-2] and senkou_a.iloc[-1] < senkou_b.iloc[-1])

def scanner():
    results = []
    for symbol in SYMBOLS:
        for tf_name, tf_interval in TIMEFRAMES.items():
            try:
                df = tv.get_hist(symbol=symbol, exchange='CME', interval=tf_interval, n_bars=100)
                if df is not None and not df.empty and detect_twist(df):
                    results.append(f"{symbol} - {tf_name} : Twist détecté 💥")
            except Exception as e:
                print(f"Erreur sur {symbol} {tf_name} : {e}")
    return "\n".join(results) if results else "Aucun twist détecté pour l’instant."
