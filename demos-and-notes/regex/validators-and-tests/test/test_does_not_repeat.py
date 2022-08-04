import unittest
from validators.does_not_repeat import *

class DoesNotRepeat(unittest.TestCase):

    def test_allow_nonrepetitive_passwords(self):
        """Optimistic assertions - Allow any password without repeated substrings greater than 4 characters"""
        self.assertTrue(does_not_repeat('hunter2'))
        self.assertTrue(does_not_repeat('correcthorsebatterystaple'))
        self.assertTrue(does_not_repeat('redredred'))


    def test_forbid_repetitive_passwords(self):
        """Pessimistic assertions - reject anything with repetitions in it"""
        self.assertFalse(does_not_repeat('DealsOrNoDeals'))
        self.assertFalse(does_not_repeat('dingding'))

if __name__ == '__main__':
    unittest.main()