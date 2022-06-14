import unittest
from Main.Recursion import Permutations


class PermutationsTest(unittest.TestCase):

    def test_case_1(self):
        permutations = Permutations.get_permutations([1, 2, 3])
        self.assertEqual(len(permutations), 6)
        self.assertTrue([1, 2, 3] in permutations)
        self.assertTrue([1, 3, 2] in permutations)
        self.assertTrue([2, 1, 3] in permutations)
        self.assertTrue([2, 3, 1] in permutations)
        self.assertTrue([3, 1, 2] in permutations)
        self.assertTrue([3, 2, 1] in permutations)

    def test_case_2(self):
        permutations = Permutations.get_permutations_swap([1, 2, 3])
        self.assertEqual(len(permutations), 6)
        print(permutations)
        self.assertTrue([1, 2, 3] in permutations)
        self.assertTrue([1, 3, 2] in permutations)
        self.assertTrue([2, 1, 3] in permutations)
        self.assertTrue([2, 3, 1] in permutations)
        self.assertTrue([3, 1, 2] in permutations)
        self.assertTrue([3, 2, 1] in permutations)
