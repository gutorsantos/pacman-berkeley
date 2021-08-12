# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from util import Stack
    stack = Stack()
    stack.push((problem.getStartState(), []))
    path = []
    visited = []
    while(not stack.isEmpty()):
        current_node, path = stack.pop()

        if(problem.isGoalState(current_node)):
            return path
        if(not current_node in visited):
            visited += [current_node]
            successors = problem.getSuccessors(current_node)
            for successor in successors:
                if(not successor[0] in visited):
                    temp_path = path + [successor[1]]
                    stack.push((successor[0], temp_path))


def breadthFirstSearch(problem):
    from util import Queue
    queue = Queue()
    queue.push((problem.getStartState(), []))
    path = []
    visited = []
    while(not queue.isEmpty()):
        current_node, path = queue.pop()

        if(problem.isGoalState(current_node)):
            return path
        if(not current_node in visited):
            visited += [current_node]
            successors = problem.getSuccessors(current_node)
            for successor in successors:
                if(not successor[0] in visited):
                    temp_path = path + [successor[1]]
                    queue.push((successor[0], temp_path))

def uniformCostSearch(problem):
    from util import PriorityQueue
    p_queue = PriorityQueue()
    p_queue.push((problem.getStartState(), [], 0), 0)
    path = []
    visited = []
    while(not p_queue.isEmpty()):
        current_node, path, c_cost = p_queue.pop()

        if(problem.isGoalState(current_node)):
            return path
        if(not current_node in visited):
            visited += [current_node]
            successors = problem.getSuccessors(current_node)
            for successor in successors:
                if(not successor[0] in visited):
                    temp_path = path + [successor[1]]
                    p_queue.push((successor[0], temp_path, successor[2]+c_cost), successor[2]+c_cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    from util import PriorityQueue
    p_queue = PriorityQueue()
    p_queue.push((problem.getStartState(), [], 0), 0)
    path = []
    visited = []
    while(not p_queue.isEmpty()):
        current_node, path, c_cost = p_queue.pop()

        if(problem.isGoalState(current_node)):
            return path
        if(not current_node in visited):
            visited += [current_node]
            successors = problem.getSuccessors(current_node)
            for successor in successors:
                if(not successor[0] in visited):
                    temp_path = path + [successor[1]]
                    p_queue.push((successor[0], temp_path, successor[2]+c_cost), successor[2]+c_cost  + heuristic(successor[0],problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
