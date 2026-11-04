import unittest
from aims.dvd import DigitalVideoDisc as DVD
from aims.search import search_by_category


class CategorySearchTest(unittest.TestCase):
    def test_category_search(self):
        items = [DVD("A", "Animation"), DVD("B", "Drama"), DVD("C", "Animation")]
        self.assertEqual(search_by_category(items, "animation"), [items[0], items[2]])
        self.assertEqual(search_by_category(items, "Action"), [])
        self.assertEqual(search_by_category([], "Drama"), [])
        self.assertEqual(len(items), 3)
