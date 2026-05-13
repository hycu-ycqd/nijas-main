"""QA unit tests for utility helpers."""
import unittest
from src.utils.helpers import slugify


class TestUtils(unittest.TestCase):

    def test_slugify_spaces(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_slugify_uppercase(self):
        self.assertEqual(slugify("UPPER"), "upper")

    def test_slugify_empty(self):
        self.assertEqual(slugify(""), "")


if __name__ == "__main__":
    unittest.main()
