#!/usr/bin/env python
"""
Name of the author(s):
- Auguste Burlats <auguste.burlats@uclouvain.be>
"""
# Import necessary libraries
import time
import sys
from copy import deepcopy
from search import *


#################
# Problem class #
#################

# Define the TowerSorting problem as a subclass of the generic Problem class
class TowerSorting(Problem):

    # Define methods specific to this problem

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        indexFullCol = []
        allActions = []

        for i in range(state.number):
            if len(state.grid[i]) == state.size:
                indexFullCol.append(i)
        nbrFullCol = len(indexFullCol)

        for i in range(state.number):
            for j in range(state.number):
                if (j != i and j not in indexFullCol):
                    allActions.append((i,j))
        

        return allActions


    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        pass




    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        pass


###############
# State class #
###############

# Define the State class
class State:

    # Initialize a State object with the number of towers, size of the grid, and the grid itself
    def __init__(self, number, size, grid, move="Init"):
        self.number = number
        self.size = size
        self.grid = grid
        self.move = move

    # Define how to output a State object as a string
    def __str__(self):
        s = self.move + "\n"
        for i in reversed(range(self.size)):
            for tower in self.grid:
                if len(tower) > i:
                    s += "".join(tower[i]) + " "
                else:
                    s += ". "
            s += "\n"
        return s

    # Define how to test if two State objects are equal
    def __eq__(self, other):
        pass

    # Define how to hash a State object
    def __hash__(self):
        pass


######################
# Auxiliary function #
######################

# Define a function to read in the instance file for the problem
def read_instance_file(filepath):
    with open(filepath) as fd:
        lines = fd.read().splitlines()

    number_tower, size_tower = tuple([int(i) for i in lines[0].split(" ")])
    initial_grid = [[] for i in range(number_tower)]
    for row in lines[1:size_tower+1]:
        elems = row.split(" ")
        for index in range(number_tower):
            if elems[index] != '.':
                initial_grid[index].append(elems[index])

    for tower in initial_grid:
        tower.reverse()

    return number_tower, size_tower, initial_grid

state1 = read_instance_file("./instances/i01")
State1 = State(state1[0], state1[1], state1[2])
myAgent = TowerSorting(State1)
print(state1)
print(myAgent.actions(State1))

"""if __name__ == "__main__":
    # Check if the instance file has been provided
    if len(sys.argv) != 2:
        print(f"Usage: ./sort_tower.py <path_to_instance_file>")
    filepath = sys.argv[1]

    # Read in the instance file
    number, size, initial_grid = read_instance_file(filepath)

    # Create an initial state for the problem
    init_state = State(number, size, initial_grid, "Init")
    problem = TowerSorting(init_state)

    # Example of search
    # Use depth-first tree search to solve the problem and record performance metrics
    start_timer = time.perf_counter()
    node, nb_explored, remaining_nodes = depth_first_tree_search(problem)
    end_timer = time.perf_counter()

    # Example of print
    # Print the path from the initial state to the goal state, as well as the performance metrics
    path = node.path()

    for n in path:
        # assuming that the __str__ function of state outputs the correct format
        print(n.state)

    print("* Execution time:\t", str(end_timer - start_timer))
    print("* Path cost to goal:\t", node.depth, "moves")
    print("* #Nodes explored:\t", nb_exp)
    print("* Queue size at goal:\t",  remaining_nodes)"""
