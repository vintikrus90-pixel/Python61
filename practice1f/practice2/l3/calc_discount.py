import unittest


def calc_discount(lvl, amount):
    if lvl == "basic":
        return amount * 0.95
    elif lvl == "silver":
        return amount * 0.90
    elif lvl == "gold":
        return amount * 0.85
    else:
        raise ValueError("неизвестный уровень")

class TestCalcDiscount(unittest.TestCase):
    def test_basic_discount(self):
        self.assertEqual(calc_discount("basic", 100), 95)

    def test_silver_discount(self):
        self.assertEqual(calc_discount("silver", 100), 90)

    def test_gold_discount(self):
        self.assertEqual(calc_discount("gold", 100), 85)

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            calc_discount("platinum", 100)


if __name__ == "__main__":
    unittest.main()