"""QA unit tests for main module."""
import unittest
from src.utils.helpers import greet, add


class TestMain(unittest.TestCase):

    def test_greet_returns_string(self):
        result = greet("QA")
        self.assertIsInstance(result, str)

    def test_greet_contains_name(self):
        result = greet("Alice")
        self.assertIn("Alice", result)

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
