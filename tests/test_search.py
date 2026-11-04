import unittest

from aims.dvd import DigitalVideoDisc as DVD
from aims.search import search_by_title


class TitleSearchTest(unittest.TestCase):
    def test_title_search_returns_matches(self):
        items = [DVD("The Lion King"), DVD("Arrival")]
        self.assertEqual(search_by_title(items, "Lion"), [items[0]])
        self.assertEqual(search_by_title(items, "missing"), [])
        self.assertEqual(search_by_title([], "Lion"), [])
        self.assertEqual([dvd.title for dvd in items], ["The Lion King", "Arrival"])

    def test_title_search_ignores_case(self):
        items = [DVD("The Lion King"), DVD("Arrival")]
        for keyword in ("lion", "LION", "LiOn"):
            with self.subTest(keyword=keyword):
                self.assertEqual(search_by_title(items, keyword), [items[0]])
