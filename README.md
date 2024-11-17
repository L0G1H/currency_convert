# Currency Convert

---

A Python library to fetch real-time currency exchange rates from [Forbes Advisor](https://www.forbes.com/advisor/money-transfer/currency-converter/) with a fallback to the `CurrencyConverter` library for reliability.

### Installation

---

```bash
pip install git+https://github.com/yourusername/currency_convert.git
```

### Dependencies

---

This library requires the following dependencies, which will be installed automatically:

- `requests`: For making HTTP requests.
- `bs4`: For parsing HTML.
- `CurrencyConverter`: For fetching exchange rates as a backup.

### Parameters

---

- `base_curr` (str): The base currency code (e.g., `USD`).
- `target_curr` (str): The target currency code (e.g., `EUR`).

### Example

---

```python
from currency_convert import get_rate, get_backup_rate

base_currency = "USD"
target_currency = "EUR"

rate = get_rate(base_currency, target_currency)
backup_rate = get_backup_rate(base_currency, target_currency)
```