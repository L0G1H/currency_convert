import requests
from bs4 import BeautifulSoup
from currency_converter import CurrencyConverter
import re


def get_rate(base_curr: str, target_curr: str) -> float:
    base_curr = base_curr.lower()
    target_curr = target_curr.lower()

    url = f"https://www.forbes.com/advisor/money-transfer/currency-converter/{base_curr}-{target_curr}/"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve data: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")

    try:
        exchange_rate_text = soup.find("h2").text
        exchange_rate_raw = re.search(r"(\d+\.\d+)", exchange_rate_text)
        if exchange_rate_raw:
            return float(exchange_rate_raw.group(1))
        else:
            raise Exception("Exchange rate format not found")
    except Exception as e:
        raise Exception(f"Error parsing exchange rate: {e}")


def get_backup_rate(base_curr: str, target_curr: str) -> float:
    base_curr = base_curr.upper()
    target_curr = target_curr.upper()

    try:
        c = CurrencyConverter()
        rate = c.convert(1, base_curr, target_curr)

        return float(rate)
    except Exception as e:
        raise Exception(f"Backup rate failed: {e}")