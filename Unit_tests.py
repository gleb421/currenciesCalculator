from currencies import Constants
from currencies_calculator import currenciesCalc
import unittest


class CurrenciesCalculator(unittest.TestCase):

    def test_res(self):
        res1 = 1 * 93.0351
        res2 = 2 * 99.0111
        res3 = 3 * 12.6911
        self.assertEqual(res1, currenciesCalc(1, 'USD'))
        self.assertEqual(res2, currenciesCalc(2, 'EUR'))
        self.assertEqual(res3, currenciesCalc(3, 'CNY'))

    def test_zero_mul(self):
        res1 = currenciesCalc(0, 'USD')
        res2 = currenciesCalc(0, 'EUR')
        res3 = currenciesCalc(0, 'CNY')
        self.assertEqual(res1, currenciesCalc(0, 'USD'))
        self.assertEqual(res2, currenciesCalc(0, 'EUR'))
        self.assertEqual(res3, currenciesCalc(0, 'CNY'))
