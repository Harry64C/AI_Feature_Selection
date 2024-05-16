from queue import PriorityQueue
import copy
import random

def evaluate(Node):
    offset = float(random.randint(0, 9)) / 10
    return random.randint(0, 100) + offset


# Node class that represents a single problem state
class Node:

    def __init__(self, features = set()):
        self.features = features
        self.accuracy = evaluate(self)

    def __lt__(self, node): # sorting function for priority queue
        return (self.accuracy) < (node.accuracy)


class Problem:
    def __init__(self, featureCnt, algorithm):
        self.featureCnt = featureCnt
        self.algorithm = algorithm

    def addToFrontier(self, curr, frontier):
        if (self.algorithm == 1): # Forward Selection
            for i in range(1, self.featureCnt+1):
                if (i not in curr.features):
                    newFeatures = copy.copy(curr.features)
                    newFeatures.add(i)
                    frontier.add(Node(newFeatures))

def printFrontier(frontier): # helper function for output
    for i in frontier:
        print("\n\tUsing feature(s)", i.features, end = " ")
        print ("accuracy is", i.accuracy, "%")


def main():
    
    totalFeatures = int(input("Welcome to Harrison Cooper Feature Selection Algorithm.\nPlease enter total number of features: "))
    algNum = int(input("Type the number of the algorithm you want to run.\n\n\tForward Selection\n\tBackward Elimination\n\tHarrison's Special Algorithm.\n"))

    
    frontier = set() # using set because lookup is much faster than a list
    
    problem = Problem(totalFeatures, algNum)
    problem.addToFrontier(Node(), frontier)

    print("initial frontier:")
    printFrontier(frontier)
    
    print("\nBeginning search.")


if __name__=="__main__": 
    main()