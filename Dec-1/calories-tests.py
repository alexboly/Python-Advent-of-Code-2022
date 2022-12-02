import unittest
from parameterized import parameterized, parameterized_class
from elfCalories import bestElf, caloriesTextToList, caloriesSumFirstThreeElves

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


    @parameterized.expand([
        ("single value", [[1]], 1),
        ("two values", [[1], [2]], 3),
        ("first has two values", [[1, 2], [2]], 5),
        ("three elves", [[1, 2], [2], [3, 5]], 13),
        ("more than three elves", [[1, 2], [2], [3, 5], [7, 9]], 27),
        ])
    def test_caloriesSumFirstThreeElves(self, name, input, expected):
        self.assertEqual(caloriesSumFirstThreeElves(input), expected)


