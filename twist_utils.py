
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def check_twist_on(symbol, tf):
    url = f"https://www.tradingview.com/chart/?symbol={symbol}&interval={tf}"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(6)
        shapes = driver.find_elements(By.CSS_SELECTOR, 'svg [fill="black"]')
        return len(shapes) > 0
    except Exception as e:
        print(f"Erreur : {e}")
        return False
    finally:
        driver.quit()
