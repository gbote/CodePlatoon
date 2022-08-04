import unittest
from validators.is_alphanumeric import *

class IsAlphaNumeric(unittest.TestCase):

    def test_is_alphanumeric(self):
        """Optimistic assertions - Valid usernames start with a letter, and then have only letters, numbers, or underscores"""
        self.assertTrue(is_alphanumeric('Seven11'))
        self.assertTrue(is_alphanumeric('a_username_with_4_underscores'))


    def test_forbid_illegal_usernames(self):
        """Pessimistic assertions - reject anything that doesn't meet the above rules"""
        self.assertFalse(is_alphanumeric('2pac'))
        self.assertFalse(is_alphanumeric('_TheMoon'))

if __name__ == '__main__':
    unittest.main()