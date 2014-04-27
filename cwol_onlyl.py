from dynamics_sim import Game
from cwol import CWOL


class CWOLOnlyL(Game):
    DEFAULT_PARAMS = CWOL.DEFAULT_PARAMS
    PLAYER_LABELS = CWOL.PLAYER_LABELS
    STRATEGY_LABELS = (CWOL.STRATEGY_LABELS[0],
                       CWOL.STRATEGY_LABELS[1] + ('Only L', ))
    EQUILIBRIA_LABELS = CWOL.EQUILIBRIA_LABELS + ('Only L', )

    def __init__(self, a, b, c_low, c_high, d, w, p, player1_prop, equilibrium_tolerance=.1):
        payoff_matrix_p1 = ((a / (1 - w), a / (1 - w), a, a / (1 - w)),
                            (a, a / (1 - w), a, a / (1 - w)),
                            (a * p + c_high * (1 - p), (a * p + c_high * (1 - p)) / (1 - p * w), a * p + c_high * (1 - p), 1 / (1 - w) * (p * a + (1 - p) * c_high)),
                            (c_low * p + c_high * (1 - p), c_low * p + c_high * (1 - p), c_low * p + c_high * (1 - p), 1 / (w * (1 - p)) * (p * c_low + (1 - p) * c_high)))

        payoff_matrix_p2 = ((b / (1 - w), b / (1 - w), b, b / (1 - w)),
                            (b, b / (1 - w), b, b / (1 - w)),
                            (b * p + d * (1 - p), (b * p + d * (1 - p)) / (1 - p * w), b * p + d * (1 - p), 1 / (1 - w) * (p * b + (1 - p) * d)),
                            (d, d, d, 1 / w * (1 - p) * d))

        payoff_matrix = [payoff_matrix_p1, payoff_matrix_p2]
        player_dist = (player1_prop, 1 - player1_prop)
        super(CWOLOnlyL, self).__init__(payoff_matrices=payoff_matrix, player_frequencies=player_dist, equilibrium_tolerance=equilibrium_tolerance)

    @classmethod
    def classify(cls, params, state, tolerance):
        threshold = 1 - tolerance
        if state[0][2] > threshold and state[1][3] > threshold:
            return 3
        else:
            return CWOL.classify(params, state, tolerance)






