__author__ = 'elubin'
from cwol import CWOL
from dynamics_sim import GameDynamicsWrapper, VariedGame
from dynamics_sim.dynamics import WrightFisher
import unittest


class TestCase(unittest.TestCase):
    def test_single_simulation(self):
        s = GameDynamicsWrapper(CWOL, WrightFisher, dynamics_kwargs=dict(mu=0.05), game_kwargs=dict(a=.85))
        s.simulate(num_gens=200)

    def test_many_simulation(self):
        s = GameDynamicsWrapper(CWOL, WrightFisher, dynamics_kwargs=dict(mu=0.1), game_kwargs=dict(a=1.8, equilibrium_tolerance=.2))
        print s.simulate_many(num_iterations=10, num_gens=1000)

    def test_vary_one(self):
        s = VariedGame(CWOL, WrightFisher)
        s.vary_param('a', 0, 2, 60, num_gens=150, num_iterations=10)

    def test_vary_d(self):
        s = VariedGame(CWOL, WrightFisher)
        s.vary_param('d', -3, -0.05, 60, num_gens=150, num_iterations=10)

    def test_vary_ch(self):
        s = VariedGame(CWOL, WrightFisher)
        s.vary_param('c_high', 4.05, 15.95, 100, num_gens=150, num_iterations=5)

    def test_vary_p(self):
        s = VariedGame(CWOL, WrightFisher)
        s.vary_param('p', 0.1, 0.9, 60, num_gens=150, num_iterations=10)

    def test_vary_dependent(self):
        p = .51
        s = VariedGame(CWOL, WrightFisher, game_kwargs=dict(p=p))
        mean_c = 7.88
        s.vary(game_kwargs=[{'c_low': (3, 12, 20)}, {'c_high': lambda o: (mean_c - o.c_low * o.p) / (1 - o.p)}], num_iterations=1, graph=True)



if __name__ == '__main__':
    unittest.main()