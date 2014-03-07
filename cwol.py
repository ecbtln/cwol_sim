from generic_wf_sim.game import Game


class CWOL(Game):
    def __init__(self, a=1, b=1, c_low=4, c_high=12, d=-10, w=0.895, p=0.51, player1_prop=0.5):
        payoff_matrix_p1 = ((a / (1 - w), a / (1 - w), a),
                            (a, a / (1 - w), a),
                            (a * p + c_high * (1 - p), (a * p + c_high * (1 - p)) / (1 - p * w), a * p + c_high * (1 - p)),
                            (c_low * p + c_high * (1 - p), c_low * p + c_high * (1 - p), c_low * p + c_high * (1 - p)))

        payoff_matrix_p2 = ((b / (1 - w), b / (1 - w), b),
                            (b, b / (1 - w), b),
                            (b * p + d * (1 - p), (b * p + d * (1 - p)) / (1 - p * w), b * p + d * (1 - p)),
                            (d, d, d))

        payoff_matrix = [payoff_matrix_p1, payoff_matrix_p2]
        player_dist = (player1_prop, 1 - player1_prop)
        super(CWOL, self).__init__(payoff_matrix=payoff_matrix, player_frequencies=player_dist)


class SimulationWrapper(object):

    def __init__(self, fixed_kwarg, vary_kwarg, vary_range, num_repetitions=500):
        pass



