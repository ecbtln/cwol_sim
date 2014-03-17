__author__ = 'elubin'
from cwol import CWOL
from dynamics_sim.dynamics import WrightFisher
from dynamics_sim import GameDynamicsWrapper

import unittest


class TestCase(unittest.TestCase):
    def test_single_simulation(self):
        s = GameDynamicsWrapper(CWOL, WrightFisher)
        s.simulate()

    def test_expected_payoff_recursion(self):
        pass



if __name__ == '__main__':
    unittest.main()