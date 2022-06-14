import Main.Recursion.StaicaseTraversalRecursion as staircase
import unittest


class StaircaseTraversalRecursionTest(unittest.TestCase):
    def test_case1_check_possible_ways(self):
        stairs = 4
        max_steps = 2
        expected = 5
        actual = staircase.staircase_traversal(stairs, max_steps)
        print(actual)
        self.assertEqual(actual, expected)
