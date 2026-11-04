import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc as DVD


class SortTest(unittest.TestCase):
    def test_sort_by_title(self):
        cart = Cart()
        cart.items = [DVD("zebra", cost=5), DVD("Arrival", cost=10), DVD("bird", cost=2)]
        cart.sort_by_title()
        self.assertEqual([dvd.title for dvd in cart.items], ["Arrival", "bird", "zebra"])
        self.assertEqual(cart.total_cost(), 17)
        Cart().sort_by_title()

    def test_sort_by_cost(self):
        cart = Cart()
        cart.items = [DVD("A", cost=10), DVD("B", cost=2), DVD("C", cost=2)]
        cart.sort_by_cost()
        self.assertEqual([dvd.title for dvd in cart.items], ["B", "C", "A"])
        self.assertEqual(cart.total_cost(), 14)
        Cart().sort_by_cost()
