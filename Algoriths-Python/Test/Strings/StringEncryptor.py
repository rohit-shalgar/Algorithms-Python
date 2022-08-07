import unittest
import Main.Strings.StringEncryptor as program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.encryptString("xyz", 2), "zab")

    def test_case_2(self):
        self.assertEqual(program.encryptString("xyz", 52), "xyz")

    def test_case_3(self):
        self.assertEqual(program.encryptString("abc", 0), "abc")

    def test_case_4(self):
        self.assertEqual(program.encryptString("xyz", 54), "zab")
