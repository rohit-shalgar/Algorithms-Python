from Main.Recursion import ProductSum
import unittest


class ProductSumTest(unittest.TestCase):

    def test_case_1(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(ProductSum.get_product_sum(test), 12)
