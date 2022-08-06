import unittest
import Main.Strings.LengthEncoding as program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.lengthEncoder("xyz", 2), "zab")

    def test_case_2(self):
        self.assertEqual(program.lengthEncoder("xyz", 52), "xyz")

    def test_case_3(self):
        self.assertEqual(program.lengthEncoder("abc", 0), "abc")

    def test_case_4(self):
        self.assertEqual(program.lengthEncoder("xyz", 54), "zab")
