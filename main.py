from queue import PriorityQueue
import copy
import random

import Validator as V # import my validator file

# def evaluate(Node):
#     offset = float(random.randint(0, 9)) / 10
#     return random.randint(0, 100) + offset


# Node class that represents a single problem state
class Node:

    def __init__(self, features = [], accuracy = 0.0, newestFet = 0):
        self.features = features
        self.accuracy = accuracy
        self.newestFet = newestFet # keeps track of most recent change in the state

    def __lt__(self, node): # sorting function for priority queue
        return (self.accuracy) < (node.accuracy)


class Problem:
    def __init__(self, featureCnt, algorithm):
        self.featureCnt = featureCnt
        self.algorithm = algorithm
        self.fetList = set()
        for i in range(1, featureCnt+1): # using set because lookup is much faster than a list
            self.fetList.add(i)

        filename = input("Enter the filename of the dataset you would like to use or press enter for the default: ")
        if (len(filename) < 10): 
            filename = "Datasets/small-test-dataset.txt"

        print("Using", filename)
        self.validator = V.Validator(filename)

    def createFrontier(self, curr): # creates the frontier from curr state and new features
        frontier = []
        if (self.algorithm == 1): # Forward Selection
            for i in self.fetList:
                newFeatures = copy.copy(curr.features)
                newFeatures.append(i)

                temp = Node(newFeatures, 0, i)
                temp.accuracy = self.validator.evaluate(newFeatures)

                frontier.append(temp)

        elif (self.algorithm == 2): # Backward Elimination
            for i in self.fetList:
                newFeatures = copy.copy(curr.features)
                newFeatures.remove(i)

                temp = Node(newFeatures, 0, i)
                temp.accuracy = self.validator.evaluate(newFeatures)

                frontier.append(temp)
        
        return frontier

def printFrontier(frontier): # helper function for output
    for i in frontier:
        print("\tUsing feature(s)", i.features, end = " ")
        print ("accuracy is", i.accuracy, "%")


def main():
    totalFeatures = int(input("Welcome to Harrison Cooper Feature Selection Algorithm.\nPlease enter total number of features: "))
    algNum = int(input("Type the number of the algorithm you want to run.\n\n\tForward Selection\n\tBackward Elimination\n\tHarrison's Special Algorithm.\n"))

    curr = Node([], 1 / totalFeatures) # initalize the starting node
    #curr.accuracy = evaluate(curr)

    if (algNum == 2):
        for i in range(1, totalFeatures+1):
            curr.features.append(i)
        print("\nUsing features", curr.features, "and a \"random\" evaluation, I get an accuracy of", curr.accuracy, '%')
    else: print("\nUsing no features and a \"random\" evaluation, I get an accuracy of", curr.accuracy, '%')

    problem = Problem(totalFeatures, algNum) # initalize the problem with input
    frontier = problem.createFrontier(curr)

    print("\nBeginning Search\n")
    printFrontier(frontier)

    allTimeBest = Node()

    while (problem.fetList): # loop while there are still new features to add
        curr = Node()

        for i in frontier:
            if (i.accuracy > curr.accuracy):
                curr = i

        problem.fetList.remove(curr.newestFet) # remove the chosen feature from featureList

        print("\nFeature set", curr.features, "was best, accuracy is", curr.accuracy, "%\n")

        if (curr.accuracy < allTimeBest.accuracy):
            print("(Warning, Accuracy has decreased!)")
        else: 
            allTimeBest = curr

        frontier = problem.createFrontier(curr)
        printFrontier(frontier)

    print("Finished search!! The best feature subset is", allTimeBest.features, "which has an accuracy of", allTimeBest.accuracy, "%")
        
main() # call main function