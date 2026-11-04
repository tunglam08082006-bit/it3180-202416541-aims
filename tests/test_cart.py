import contextlib
import io
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc as DVD


class CartTest(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            for index in range(20):
                self.assertTrue(cart.add_digital_video_disc(DVD(f"Disc {index}")))
            self.assertFalse(cart.add_digital_video_disc(DVD("Disc 21")))
        self.assertEqual(len(cart.items), 20)

    def test_total_cost(self):
        cart = Cart()
        self.assertEqual(cart.total_cost(), 0)
        cart.items.extend([DVD("A", cost=19.95), DVD("B", cost=24.99), DVD("C", cost=18.95)])
        self.assertAlmostEqual(cart.total_cost(), 63.89)
