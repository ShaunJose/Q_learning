# author: Shaun Jose

# Description:
# Contrains class Q_Model

class Q_Model:

    # Initialise probabilities of person being dead
    PROB_EX_DEAD = 1/10 # probability person dies due to exercise
    PROB_EX_ALIVE = 1 - PROB_EX_DEAD
    PROB_RE_DEAD = 1/100 # probability person dies due to relaxing
    PROB_RE_ALIVE = 1 - PROB_RE_DEAD

    # Initialise dictionaries for R-matrix and probability values
    # States: F -> fit, U -> Unfit, D -> Deads
    # Actions: E -> Exercies, R -> Relax
    R_DICT = {
      "F,E,F" : 8,
      "F,E,U" : 8,
      "F,E,D" : 0,
      "F,R,F" : 10,
      "F,R,U" : 10,
      "F,R,D" : 0,
      "U,E,F" : 0,
      "U,E,U" : 0,
      "U,E,D" : 0,
      "U,R,F" : 5,
      "U,R,U" : 5,
      "U,R,D" : 0,
      "D,E,F" : 0,
      "D,E,U" : 0,
      "D,E,D" : 0,
      "D,R,F" : 0,
      "D,R,U" : 0,
      "D,R,D" : 0, }

    P_DICT = {
      "F,E,F" : 0.99 * PROB_EX_ALIVE,
      "F,E,U" : 0.01 * PROB_EX_ALIVE,
      "F,E,D" : PROB_EX_DEAD,
      "F,R,F" : 0.7 * PROB_RE_ALIVE,
      "F,R,U" : 0.3 * PROB_EX_ALIVE,
      "F,R,D" : PROB_RE_DEAD,
      "U,E,F" : 0.2 * PROB_EX_ALIVE,
      "U,E,U" : 0.8 * PROB_EX_ALIVE,
      "U,E,D" : PROB_EX_DEAD,
      "U,R,F" : 0 * PROB_RE_ALIVE,
      "U,R,U" : 1 * PROB_RE_ALIVE,
      "U,R,D" : PROB_RE_DEAD,
      "D,E,F" : 0,
      "D,E,U" : 0,
      "D,E,D" : 1,
      "D,R,F" : 0,
      "D,R,U" : 0,
      "D,R,D" : 1, }

    # Constructor
    def __init__(self, n, gamma, s):
        self.n = n # q-matrix number
        self.gamma = gamma # gamma value ("learning rate")
        self.s = s # State
