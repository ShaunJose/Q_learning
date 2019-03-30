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
        self.n = int(n) # q-matrix number
        self.gamma = float(gamma) # gamma value ("learning rate")
        self.s = s # State
        self.q = q # get q matrix (in the form of a dictionary)


    # Finds qn using function _update_q, and then prints relevant values of qn
    def compute_qn(self):
        """
        Finds qn for the particular Q_Model

        return: The value of qn
        """

        print(self.q)

        # update q matrix to qn
        _update_q()

        # print qn(s, exercise) & qn(s, relax)
        print("qn(" + s + ", exercise): " + q(s + "," + "E"))
        print("qn(" + s + ", relax): " + q(s + "," + "R"))


    # updates the q dictionary to qn
    # def _update_q():

        # update q0 to qn, it not already qn
        # while(self.n > 0):

        #TODO: make that function call a max function for the equation
