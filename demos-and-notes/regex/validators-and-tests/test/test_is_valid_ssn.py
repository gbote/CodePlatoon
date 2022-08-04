import unittest
from validators.is_valid_ssn import *

class IsValidSSN(unittest.TestCase):

    def test_is_valid_ssn(self):
        """Optimistic assertions - Allow 9 digit numbers, maybe with dashes"""
        self.assertTrue(is_valid_ssn('123456789'))
        self.assertTrue(is_valid_ssn('987-65-4321'))


    def test_forbid_non_ssn(self):
        """Pessimistic assertions - reject anything that's not an SSN"""
        self.assertFalse(is_valid_ssn('800-555-1234'))
        self.assertFalse(is_valid_ssn('2fast2furious'))
        self.assertFalse(is_valid_ssn('98765-4321'))

if __name__ == '__main__':
    unittest.main()