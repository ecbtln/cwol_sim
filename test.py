__author__ = 'elubin'
from cwol import CWOL
from dynamics_sim import GameDynamicsWrapper
from dynamics_sim.dynamics import WrightFisher
import unittest


class TestCase(unittest.TestCase):
    def test_single_simulation(self):
        s = GameDynamicsWrapper(CWOL, WrightFisher, dynamics_kwargs=dict(mu=0.07), game_kwargs=dict())
        s.simulate()

    def test_many_simulation(self):
        s = GameDynamicsWrapper(CWOL, WrightFisher, dynamics_kwargs=dict(mu=0.07), game_kwargs=dict())
        print s.simulate_many(num_iterations=1000, num_gens=100)


if __name__ == '__main__':
    unittest.main()