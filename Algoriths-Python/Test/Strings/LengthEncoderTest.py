import Main.Strings.LengthEncoder as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "AAAAAAAAAAAAABBCCCCDD"
        expected = "9A4A2B4C2D"
        actual = program.runLengthEncoding(string)
        self.assertEqual(actual, expected)
