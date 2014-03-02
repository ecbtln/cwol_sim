__author__ = 'elubin'

import unittest
from cwol import CWOLWrightFisher


class TestCase(unittest.TestCase):
    def test_likelihood(self):
        w = CWOLWrightFisher()
        print w.payoff_matrix

if __name__ == '__main__':
    unittest.main()