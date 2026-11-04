"""Search helpers return a new list without changing the input."""


def search_by_title(items, keyword):
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
