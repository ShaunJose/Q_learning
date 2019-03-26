# author: Shaun Jose

# Description:
# Contrains class Q_Model

#Imports
from constants import PROB_EX_DEAD
from constants import PROB_EX_ALIVE
from constants import PROB_RE_DEAD
from constants import PROB_RE_ALIVE
from constants import NUM_STATES
from constants import NUM_ACTIONS
from constants import STATES
from constants import ACTIONS
from constants import R_DICT
from constants import P_DICT

class Q_Model:

    # Constructor
    def __init__(self, n, gamma, s, q):
        self.n = n # q-matrix number
        self.gamma = gamma # gamma value ("learning rate")
        self.s = s # State
        self.q = q # get q matrix


    # Finds q_n
    def find_qn(self):
        """
        Finds qn for the particular Q_Model

        return: The value of qn
        """

        print(self.q)
