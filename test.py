import unittest
import main


class TestCalc(unittest.TestCase):
    def test_button1(self):
        self.assertTrue(main.var > '1')

    def test_ms(self):
        self.assertEqual(main.memory, main.var)

    def test_c(self):
        self.assertTrue(main.var == '')

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            float(main.A / main.a)

    def test_multi(self):
        self.assertEqual((main.a * main.A), 0)

    def test_min(self):
        self.assertTrue(main.a - main.A > 0)

    def test_sum(self):
        self.assertFalse(main.a + main.A < 0)

    def test_pm(self):
        if main.var > '0':
            self.assertFalse(main.var < '0')
        else:
            self.assertFalse(main.var > '0')

    def test_point(self):
        self.assertTrue(main.var[0] != '.')

  