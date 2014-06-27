from dynamics_sim import Game


class CWOL(Game):
    DEFAULT_PARAMS = dict(a=1, b=1, c_low=4, c_high=12, d=-10, w=0.895, p=0.51, player1_prop=0.5)
    PLAYER_LABELS = ('Player 1', 'Player 2')
    STRATEGY_LABELS = (('CWOL', 'CWL', 'C if Low', 'All D'),
                       ('Exit if Look', 'Exit if Defect', 'Always Exit'))
    EQUILIBRIA_LABELS = ('CWL', 'CWOL', 'All D')

    def __init__(self, a, b, c_low, c_high, d, w, p, player1_prop, equilibrium_tolerance=0.1):
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
        super(CWOL, self).__init__(payoff_matrices=payoff_matrix, player_frequencies=player_dist, equilibrium_tolerance=equilibrium_tolerance)

    @classmethod
    def classify(cls, params, state, tolerance):
        # for convenience, we will guarantee that the state is normalized already to proportions, not absolute number of players
        # CWL
        p = params
        threshold = 1 - tolerance

        if state[1][1] >= threshold and state[0][0] + state[0][1] >= threshold:
            # CWL
            return 0
        elif state[0][0] >= threshold and state[1][0] + state[1][1] >= threshold and \
                                p.a / (1 - p.w) >= (p.p * p.a + (1 - p.p) * p.c_high) / (1 - p.p * p.w * state[1][1]) - tolerance:
            # CWOL
            return 1
        elif state[0][3] >= threshold and \
            p.p * p.c_low + (1 - p.p) * p.c_high >= (1 - state[1][2]) * p.a / (1 - p.w) + state[1][2] * p.a - tolerance and \
            p.p * p.c_low + (1 - p.p) * p.c_high >= state[1][1] * p.a / (1 - p.w) + (1 - state[1][1]) * p.a - tolerance and \
            p.p * p.c_low + (1 - p.p) * p.c_high >= state[1][0] * (p.a * p.p + p.c_high * (1 - p.p)) + state[1][0] * (p.a * p.p + p.c_high * (1 - p.p) / (1 - p.p * p.w)) + state[1][2] * (p.a * p.p + p.c_high * (1 - p.p)) - tolerance:
            return 2
        # elif state[0][3] > threshold and state[1][0] > threshold:
        #     # ALL D, since its not CWOL
        #     return 2
        else:
            return super(CWOL, cls).classify(params, state, tolerance)






