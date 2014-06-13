__author__ = 'elubin'
from cwol import CWOL
from cwol_onlyl import CWOLOnlyL
from dynamics_sim import GameDynamicsWrapper, VariedGame
from dynamics_sim.dynamics import WrightFisher, Moran
import unittest


class TestCase(unittest.TestCase):
    def test_single_simulation_moran(self):
        s = GameDynamicsWrapper(CWOLOnlyL, Moran, dynamics_kwargs=dict(pop_size=3000), game_kwargs=dict(a=0.2, equilibrium_tolerance=.5))
        s.simulate(num_gens=30000)

    def test_single_simulation(self):
        s = GameDynamicsWrapper(CWOL, WrightFisher, game_kwargs=dict())
        s.simulate(num_gens=300)

    def test_many_simulation(self):
        s = GameDynamicsWrapper(CWOL, WrightFisher, dynamics_kwargs=dict(), game_kwargs=dict(a=.2, equilibrium_tolerance=.2))
        print s.simulate_many(num_iterations=10, num_gens=150)

    def test_vary_one(self):
        s = VariedGame(CWOL, WrightFisher)
        s.vary_param('a', (0, 2, 60), num_gens=250, num_iterations=5)

    def test_vary_d(self):
        s = VariedGame(CWOLOnlyL, WrightFisher, game_kwargs=dict(equilibrium_tolerance=0.4))
        s.vary_param('d', (-3, -0.05, 60), num_gens=1000, num_iterations=5)

    def test_unclassified_d(self):
        s = GameDynamicsWrapper(CWOLOnlyL, WrightFisher, game_kwargs=dict(d=-1.0))
        s.simulate(num_gens=500)

    def test_vary_ch(self):
        s = VariedGame(CWOL, WrightFisher)
        s.vary_param('c_high', (4.05, 20.95, 200), num_gens=150, num_iterations=5)

    def test_vary_p(self):
        s = VariedGame(CWOL, WrightFisher)
        s.vary_param('p', (0.1, 0.9, 60), num_gens=150, num_iterations=10)

    def test_vary_dependent(self):
        s = VariedGame(CWOL, WrightFisher, game_kwargs=dict(equilibrium_tolerance=0.1))
        s.vary(game_kwargs=[{'c_low': (3, 12, 50)}, {'c_high': lambda o: (7.88 - o.c_low * o.p) / (1 - o.p)}], num_iterations=10, graph=True)

    def test_3d_graph(self):
        s = VariedGame(CWOL, WrightFisher)
        s.vary_2params('a', (0, 2, 30), 'b', (0, 5, 30), num_iterations=2, num_gens=150)

    def test_3d_graphb(self):
        s = VariedGame(CWOL, WrightFisher)
        s.vary_2params('c_high', (4.05, 20.95, 35), 'p', (0.1, 0.9, 35), num_iterations=2, num_gens=150)

    def test_validate_classifier(self):
        CWOL.validate_classifier(timeout=60)

if __name__ == '__main__':
    unittest.main()