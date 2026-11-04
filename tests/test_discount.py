import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc as DVD


class DiscountTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.items.append(DVD("Example", cost=100))

    def test_discounted_total(self):
        self.assertEqual(self.cart.total_cost_with_discount(20), 80)
        self.assertEqual(self.cart.total_cost_with_discount(0), 100)
        self.assertEqual(self.cart.total_cost_with_discount(100), 0)

    def test_reject_invalid_percent(self):
        for percent in (-1, 150):
            with self.subTest(percent=percent), self.assertRaises(ValueError):
                self.cart.total_cost_with_discount(percent)
