# this file must be named starting with 'test'
import unittest
from validators.is_not_password import *

class IsNotPassword(unittest.TestCase):

# all test functions must start with 'test'
    def test_allow_anything_but_password(self):
        """Optimistic assertions - allow anything that doesn't contain password"""
        self.assertTrue(is_not_password('letmein'))
        self.assertTrue(is_not_password('codeword'))

    def test_forbid_password(self):
        """Pessimistic assertions - forbid passwords that contain password"""
        self.assertFalse(is_not_password('password'))
        self.assertFalse(is_not_password('pAsSwOrD'))

# the file you called from the command line is the __main__ module. other files that get imported are not the __main__ module
if __name__ == '__main__':
    unittest.main()