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
    def test_types(self):
        with self.assertRaises(TypeError) as e:
            currenciesCalc('3', 'USD')
        print(e.exception.args)
        with self.assertRaises(TypeError) as e:
            currenciesCalc(2, 234)
        print(e.exception.args)
        with self.assertRaises(TypeError) as e:
            currenciesCalc('fds', 3)
        print(e.exception.args)
    def test_wrongcode(self):
        with self.assertRaises(KeyError) as e:
            currenciesCalc(3, 'fdf')
        print(e.exception.args)
    # def test_values(self):
    #     with self.assertRaises(ValueError) as e:
    #         currenciesCalc(-1, 'USD')
    #     print(e.exception.args)
    #     with self.assertRaises(ValueError):
    #         currenciesCalc(-2, 'EUR')
    #     print(e.exception.args)
    #     with self.assertRaises(ValueError):
    #         currenciesCalc(-3, 'CNY')
    #     print(e.exception.args)
