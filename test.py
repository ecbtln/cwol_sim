__author__ = 'elubin'
from cwol import CWOL
from dynamics_sim import GameDynamicsWrapper
from dynamics_sim.dynamics import WrightFisher
import unittest


class TestCase(unittest.TestCase):
    def test_single_simulation(self):
        s = GameDynamicsWrapper(CWOL, WrightFisher, dynamics_kwargs=dict(mu=0.07), game_kwargs=dict())
        s.simulate()


if __name__ == '__main__':
    unittest.main()