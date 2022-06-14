from Main.Recursion import PowerSet
import unittest


class PowerSetTest(unittest.TestCase):

    def test_case_1(self):
        power_sets = PowerSet.get_power_set([1, 2, 3])
        print(power_sets)
        self.assertEqual(8, len(power_sets))
        self.assertTrue([] in power_sets)
        self.assertTrue([1] in power_sets)
        self.assertTrue([2] in power_sets)
        self.assertTrue([3] in power_sets)
        self.assertTrue([1, 2] in power_sets)
        self.assertTrue([1, 3] in power_sets)
        self.assertTrue([1, 2, 3] in power_sets)
        self.assertTrue([1, 3] in power_sets)
        self.assertTrue([2, 3] in power_sets)

    def test_case_2_optimized(self):
        power_sets = PowerSet.get_power_sets_optimized([1, 2, 3])
        print(power_sets)
        self.assertEqual(8, len(power_sets))
        self.assertTrue([] in power_sets)
        self.assertTrue([1] in power_sets)
        self.assertTrue([2] in power_sets)
        self.assertTrue([3] in power_sets)
        self.assertTrue([2, 1] in power_sets)
        self.assertTrue([3, 1] in power_sets)
        self.assertTrue([3, 2, 1] in power_sets)
        self.assertTrue([3, 1] in power_sets)
        self.assertTrue([3, 2] in power_sets)
