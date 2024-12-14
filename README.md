# Currency Convert
A simple Python module to fetch real-time currency exchange rates from [Forbes Advisor](https://www.forbes.com/advisor/money-transfer/currency-converter/) with a fallback to the `CurrencyConverter` library.

## Installation
```bash
pip install git+https://github.com/L0G1H/currency_convert.git
```

## Parameters
- `base_curr` (str): The base currency code (e.g., `USD`).
- `target_curr` (str): The target currency code (e.g., `EUR`).

## Example
```python
from currency_convert import get_exchange_rate, get_forbes_rate, get_fallback_rate

base_currency = "USD"
target_currency = "EUR"

rate = get_exchange_rate(base_currency, target_currency) # Returns forbes, if fails returns fallback
backup_rate = get_forbes_rate(base_currency, target_currency) # Returns forbes
safe_rate = get_fallback_rate(base_currency, target_currency) # Returns fallback
```
## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.