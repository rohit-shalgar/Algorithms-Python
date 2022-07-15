from Main.Recursion import PhoneNumber
import unittest


class PhoneNumberTest(unittest.TestCase):

    def test_case1_getPhoneNumbers(self):
        sample_test_input = "1905"
        phone_numbers: list = PhoneNumber.get_phone_numbers(sample_test_input)
        expected = ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"]
        self.assertTrue(len(phone_numbers), 12)
        self.assertEquals(expected, phone_numbers)
