
from config import SYMBOLS, TIMEFRAMES
from twist_utils import check_twist_on

if __name__ == "__main__":
    for symbol in SYMBOLS:
        for tf in TIMEFRAMES:
            found = check_twist_on(symbol, tf)
            if found:
                print(f"🟢 Twist détecté : {symbol} @ {tf}")
