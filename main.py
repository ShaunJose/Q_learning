# author: Shaun Jose

# Description:
# Solving the problem (in problem specification) using Q-learning in python.

# Imports
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
from Q_mod import Q_Model

# q0 matrix
q0 = None

# Function that Initialises and returns the q0 dictionary
def _init_q0():
  """
  Initialises the q matrix for the first time

  return: A dictionary with q_matrix values
  """

  q = {} # initialise q - dictionary

  # Add values to the q dict
  for i in range(NUM_STATES):
      curr_state = STATES[i] # get state
      for j in range(NUM_ACTIONS):
          curr_action = ACTIONS[j] # get action
          Q_key = curr_state + "," + curr_action #make dict key
          sum = 0
          for k in range(NUM_STATES):
              next_state = STATES[k]
              R_P_key = Q_key + "," + next_state
              sum += P_DICT[R_P_key] * R_DICT[R_P_key]
          #store sum with appropriate key in q
          q[Q_key] = sum

  return q


# Takes input values n, gamma & s from the user
def _acceptValues(q0):
    """
    Takes in values n (q-matrix number), gamma and s(state) from the user

    return: None
    """

    exit = False # Symbolizes whether user wants to exit or not

    # Accept n, gamma and s until user is done
    while(not exit):
        userInput = input("Enter e to exit, anything else to continue: ")
        # Check whether user wants to exit
        if userInput == "e":
            exit = True;
            continue # go to next iteration
        # else:
        # accept valid values
        n = -1
        while n < 0: # input n accepter
            n = int(input("Input valid n: "))
        gamma = -1
        while gamma < 0 or gamma > 1: # input gamma accepter
            gamma = float(input("Input valid \u03B3: "))
        s = "Q"
        while s != 'F' and s != 'U' and s != 'D': # input s accepter
            s = input("Input valid s \nfit -> F\nunfit -> U\ndead -> D\n ")
        model = Q_Model(n, gamma, s, q0)
        model.compute_qn()


# Main method
if __name__ == "__main__":
    q0 = _init_q0()
    _acceptValues(q0) # Take input values for q_learning
