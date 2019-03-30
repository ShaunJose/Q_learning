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
        # _update_q()
        self.Q_max("F")

        # print qn(s, exercise) & qn(s, relax)
        print("qn(" + self.s + ", exercise): " + str(self.q[self.s + "," + "E"]))
        print("qn(" + self.s + ", relax): " + str(self.q[self.s + "," + "R"]))


    # updates the q dictionary to qn
    def _update_q(self):

        new_q = {} # copy of new dictionary where new values will be stored

        # update q0 to qn, it not already qn
        while self.n > 0: # n times
            for i in range(NUM_STATES): # through states
                curr_state = STATES[i] # get state
                for j in range(NUM_ACTIONS): # through actions
                    curr_action = ACTIONS[j] # get action
                    Q_key = curr_state + "," + curr_action # make dict key
                    sum = 0 # initialise sum
                    for k in range(NUM_STATES): # loop for updating new_q
                        state = STATES[k]
                        P_key = Q_key + "," + state
                        sum += P_DICT[P_key] * Q_max(state)
                    new_q[Q_key] = self.q[Q_key] + self.gamma * sum # update new_q's values
            self.q = new_q # set q to the update q dictionary
            self.n -= 1 # decrement n by 1

    # finds the max value of q(state, action), for all actions, and returns that value
    def Q_max(self, state):

        max = float('-inf') # set max to negative infinity

        print(max > -2) # False
        print(max < -2) # True


        # for i in range(NUM_ACTIONS)
