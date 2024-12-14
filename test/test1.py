import unittest
from unittest.mock import patch
from currency_convert.currency_convert import get_fallback_rate, get_forbes_rate, get_exchange_rate


class TestCurrencyConverter(unittest.TestCase):
    def test_same_currency_forbes_rate(self):
        result = get_forbes_rate("USD", "USD")
        self.assertEqual(result, 1.0)

    def test_same_currency_fallback_rate(self):
        result = get_fallback_rate("USD", "USD")
        self.assertEqual(result, 1.0)

    @patch("currency_convert.currency_convert.requests.get")
    def test_forbes_rate_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.content = b'<h2>1 USD = 0.85 EUR</h2>'
        result = get_forbes_rate("USD", "EUR")
        self.assertEqual(result, 0.85)

    @patch("currency_convert.currency_convert.requests.get")
    def test_forbes_rate_failure(self, mock_get):
        mock_get.side_effect = Exception("Connection error")
        result = get_forbes_rate("USD", "EUR")
        self.assertIsNone(result)

    @patch("currency_convert.currency_convert.currency_converter.convert")
    def test_fallback_rate_success(self, mock_convert):
        mock_convert.return_value = 0.85
        result = get_fallback_rate("USD", "EUR")
        self.assertEqual(result, 0.85)

    @patch("currency_convert.currency_convert.currency_converter.convert")
    def test_fallback_rate_failure(self, mock_convert):
        mock_convert.side_effect = Exception("Conversion error")
        result = get_fallback_rate("USD", "EUR")
        self.assertIsNone(result)

    def test_exchange_rate_chain(self):
        with patch("currency_convert.currency_convert.get_forbes_rate") as mock_forbes:
            with patch("currency_convert.currency_convert.get_fallback_rate") as mock_fallback:
                mock_forbes.return_value = None
                mock_fallback.return_value = 0.85
                result = get_exchange_rate("USD", "EUR")
                self.assertEqual(result, 0.85)


if __name__ == "__main__":
    unittest.main()