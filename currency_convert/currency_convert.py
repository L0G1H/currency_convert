import requests
from bs4 import BeautifulSoup
from currency_converter import CurrencyConverter
import re
from typing import Optional
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
currency_converter = CurrencyConverter()


def get_forbes_rate(base_currency: str, target_currency: str) -> Optional[float]:
    base_currency = base_currency.lower()
    target_currency = target_currency.lower()

    if base_currency == target_currency:
        return 1.0

    url = f"https://www.forbes.com/advisor/money-transfer/currency-converter/{base_currency}-{target_currency}/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        exchange_rate_text = soup.find("h2").text
        exchange_rate_match = re.search(r"(\d+\.\d+)", exchange_rate_text)

        if exchange_rate_match:
            return float(exchange_rate_match.group(1))

    except Exception as error:
        logger.error(f"Forbes rate failed: {str(error)}")
        return None


def get_fallback_rate(base_currency: str, target_currency: str) -> Optional[float]:
    base_currency = base_currency.upper()
    target_currency = target_currency.upper()

    if base_currency == target_currency:
        return 1.0

    try:
        rate = currency_converter.convert(1, base_currency, target_currency)
        return float(rate)
    except Exception as error:
        logger.error(f"Fallback rate failed: {str(error)}")
        return None

def get_exchange_rate(base_currency: str, target_currency: str) -> Optional[float]:
    rate = (get_forbes_rate(base_currency, target_currency) or
            get_fallback_rate(base_currency, target_currency) or
            None)

    return rate


if __name__ == "__main__":
    a = get_exchange_rate("EUR", "RUB")
    print(a)