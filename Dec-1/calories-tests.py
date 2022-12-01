import unittest
from parameterized import parameterized, parameterized_class
from elfCalories import bestElf, caloriesTextToList

class TestElfCalories(unittest.TestCase):

    @parameterized.expand([
        ("single value", [[1]], 1),
        ("two values", [[1], [2]], 2),
        ("first has two values", [[1, 2], [2]], 3),
        ])
    def test_calories(self, name, input, expected):
        self.assertEqual(bestElf(input), expected)


    @parameterized.expand([
        ("single value", """1""", [[1]]),
        ("single different value", """2""", [[2]]),
        ("two values", """1
2""", [[1, 2]]),
        ("first has two values", """1
2

3""", [[1, 2], [3]]),
        ])
    def test_fromCaloriesTextToList(self, name, input, expected):
        self.assertEqual(caloriesTextToList(input), expected)
