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
    """Search the deepest nodes in the search tree first."""
    path = []
    visited = []
    myStack = util.Stack()
    myStack.push((problem.getStartState(), []))

    while not myStack.isEmpty():
        current, path = myStack.pop()
        if current not in visited:
            visited.append(current)

            if problem.isGoalState(current):
                return path

            successors = problem.getSuccessors(current)
            for nextLocation, nextDirection, cost in successors:
                if nextLocation not in visited:
                    myStack.push((nextLocation, path + [nextDirection]))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    path = []
    visited = []
    myQueue = util.Queue()
    myQueue.push((problem.getStartState(), []))

    while not myQueue.isEmpty():
        current, path = myQueue.pop()
        if current not in visited:
            visited.append(current)
            if problem.isGoalState(current):
                return path

            successors = problem.getSuccessors(current)

            for nextLocation, nextDirection, cost in successors:
                if nextLocation not in visited:
                    myQueue.push((nextLocation, path + [nextDirection]))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    path = []
    visited = []
    myPriorityQueue = util.PriorityQueue()
    myPriorityQueue.push((problem.getStartState(), [], 0), 0)

    while not myPriorityQueue.isEmpty():
        current, path, currentCost = myPriorityQueue.pop()
        if current not in visited:
            visited.append(current)

            if problem.isGoalState(current):
                return path

            successors = problem.getSuccessors(current)
            for nextLocation, nextDirection, cost in successors:
                if nextLocation not in visited:
                    priority = currentCost + cost
                    myPriorityQueue.push((nextLocation, path + [nextDirection], priority), priority)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    path = []
    visited = []
    myPriorityQueue = util.PriorityQueue()
    myPriorityQueue.push((problem.getStartState(), [], 0), 0)

    while not myPriorityQueue.isEmpty():
        current, path, currentCost = myPriorityQueue.pop()
        if current not in visited:
            visited.append(current)

            if problem.isGoalState(current):
                return path

            successors = problem.getSuccessors(current)
            for nextLocation, nextDirection, cost in successors:
                if nextLocation not in visited:
                    newCost = currentCost + cost
                    heuristicCost = newCost + heuristic(nextLocation, problem)
                    myPriorityQueue.push((nextLocation, path + [nextDirection], newCost), heuristicCost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
