import unittest
from parameterized import parameterized, parameterized_class
from elfCalories import bestElf

class TestElfCalories(unittest.TestCase):

    @parameterized.expand([
        ("single value", [[1]], 1),
        ("two values", [[1], [2]], 2),
        ("first has two values", [[1, 2], [2]], 3),
        ])
    def test_calories(self, name, input, expected):
        self.assertEquals(bestElf(input), expected)

