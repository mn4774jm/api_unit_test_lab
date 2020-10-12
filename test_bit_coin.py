import unittest
from unittest import TestCase
from unittest.mock import patch

import bit_coin

class TestBitExchange(TestCase):

    @patch('bit_coin.request_rates')
    def test_bitcoin_to_USD(self, mock_rates):
        mock_rate = 11000
        example_api_response = {'15m': 11557.8, 'last': 11557.8, 'buy': mock_rate, 'sell': 11557.8, 'symbol': '$'}
        mock_rates.side_effect = [ example_api_response ]
        converted = bit_coin.convert_BTC_to_target(100, 'USD')
        self.assertEqual(1100000, converted)


if __name__ == '__main__':
    unittest.main()