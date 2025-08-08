import unittest

from src.main import adder


class TestMyFunctions(unittest.TestCase):
    def test_adder_simple_by_both_positive(self):
        self.assertEqual(adder(1, 1), 2)
        self.assertEqual(adder(2, 2), 4)


if __name__ == "__main__":
    unittest.main()
