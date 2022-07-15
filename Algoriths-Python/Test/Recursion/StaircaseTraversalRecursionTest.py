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

    def test_case2_check_possible_ways_optimized_with_dictionary(self):
        stairs = 4
        max_steps = 3
        expected = 7
        actual = staircase.staircase_traversal_optimized(stairs, max_steps)
        print(actual)
        self.assertEqual(actual, expected)

    def test_case3_check_possible_ways_optimized_with_dictionary(self):
        stairs = 4
        max_steps = 3
        expected = 7
        actual = staircase.staircase_traversal_dp(stairs, max_steps)
        print(actual)
        self.assertEqual(actual, expected)

    def test_case4_check_possible_ways_sliding_window(self):
        stairs = 4
        max_steps = 3
        expected = 7
        actual = staircase.staircase_traversal_sliding_window(stairs, max_steps)
        print(actual)
        self.assertEqual(actual, expected)