# author: Shaun Jose

# Description:
# Solving the problem (in problem specification) using Q-learning in python.


# Takes input values n, gamma & s from the user
def acceptValues():
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
        # accept values
        n = input("Input n: ")
        gamma = input("Input gamma: ")
        s = input("Input s: ")



# Main method
if __name__ == "__main__":
    acceptValues() # Take input values for q_learning
