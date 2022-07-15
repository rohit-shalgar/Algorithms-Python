import unittest
import Main.Arrays.SortedSquaredArray as program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [-5, -4, -3, -2, -1]
        expected = [1, 4, 9, 16, 25]
        actual = program.sortedSquaredArray(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [-5, -4, -3, -2, -1]
        expected = [1, 4, 9, 16, 25]
        actual = program.sortedSquaredArrayOpt(input)
        self.assertEqual(expected,actual)
