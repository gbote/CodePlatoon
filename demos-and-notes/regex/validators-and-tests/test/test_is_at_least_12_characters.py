# this file must be named starting with 'test'
import unittest
from validators.is_at_least_12_characters import *

class IsAtLeast12Characters(unittest.TestCase):

# all test functions must start with 'test'
    def test_allow_anything_at_least_12_characters(self):
        """Optimistic assertions - allow anything that doesn't contain password"""
        self.assertTrue(is_at_least_12_characters('correcthorsebatterystaple'))
        self.assertTrue(is_at_least_12_characters('dragonprincess'))

    def test_forbid_short_passwords(self):
        """Pessimistic assertions - forbid short passwords"""
        self.assertFalse(is_at_least_12_characters('brevity'))
        self.assertFalse(is_at_least_12_characters(''))
# the file you called from the command line is the __main__ module. other files that get imported are not the __main__ module
if __name__ == '__main__':
    unittest.main()