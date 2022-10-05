import unittest
import Calculator

class TestCalc(unittest.TestCase):
    def test_secist(self):
        result = Calculator.secist(10,5)
        self.assertEqual(result,15)











    def test_odecist(self):
        self.assertEqual(Calculator.odecist(12,6),6)
        self.assertEqual(Calculator.odecist(6, 6), 0)
        self.assertEqual(Calculator.odecist(-1, 1), -2)
        self.assertEqual(Calculator.odecist(1, -1), 2)
        self.assertEqual(Calculator.odecist(100, 1), 99)



