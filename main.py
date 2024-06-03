from queue import PriorityQueue
import copy

import Validator as V # import my validator file


# Node class that represents a single problem state
class Node:

    def __init__(self, features = [], newestFet = 0):
        self.features = features
        self.accuracy = 0.0
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

        filename = input("Type in the name of the file to test: ")
        if (len(filename) < 10): 
            # filename = "Datasets/small-test-dataset.txt"
            # filename = "Datasets/large-test-dataset.txt"
            filename = "Datasets/CS170_Spring_2024_Small_data__19.txt"
            # filename = "Datasets/CS170_Spring_2024_Large_data__19.txt"
            
        # print("Using", filename)
        self.validator = V.Validator(filename)

    def createFrontier(self, curr): # creates the frontier from curr state and new features
        frontier = []
        if (self.algorithm == 1): # Forward Selection
            for i in self.fetList:
                newFeatures = copy.copy(curr.features)
                newFeatures.append(i)

                temp = Node(newFeatures, i)
                temp.accuracy = self.validator.evaluate(newFeatures)

                frontier.append(temp)

        elif (self.algorithm == 2): # Backward Elimination
            for i in self.fetList:
                newFeatures = copy.copy(curr.features)
                newFeatures.remove(i)

                temp = Node(newFeatures, i)
                temp.accuracy = self.validator.evaluate(newFeatures)

                frontier.append(temp)
        
        return frontier

def printFrontier(frontier): # helper function for output
    for i in frontier:
        print("\tUsing feature(s)", i.features, end = " ")
        print ("accuracy is", i.accuracy)


def main():
    # totalFeatures = int(input("Welcome to Harrison Cooper Feature Selection Algorithm.\nPlease enter total number of features: "))
    print("Welcome to Harrison Cooper Feature Selection Algorithm.")
    totalFeatures = 10
    algNum = int(input("Type the number of the algorithm you want to run.\n\n\tForward Selection\n\tBackward Elimination\n\tHarrison's Special Algorithm.\n"))

    curr = Node() # initalize the starting node

    if (algNum == 2):
        for i in range(1, totalFeatures+1):
            curr.features.append(i)

    problem = Problem(totalFeatures, algNum) # initalize the problem with input
    curr.accuracy = problem.validator.evaluate()

    if (algNum == 2):
        print("\nUsing features", curr.features, ", the accuracy is", curr.accuracy)
    else: print("\nRunning nearest neighbor with no features (default rate), using “leaving-one-out” evaluation, I get an accuracy of ", curr.accuracy)

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

        print("\nFeature set", curr.features, "was best, accuracy is", curr.accuracy, "\n")

        if (curr.accuracy < allTimeBest.accuracy):
            print("(Warning, Accuracy has decreased! Continuing search in case of local maxima)")
        else: 
            allTimeBest = curr

        frontier = problem.createFrontier(curr)
        printFrontier(frontier)

    print("Finished search!! The best feature subset is", allTimeBest.features, "which has an accuracy of", allTimeBest.accuracy)
        
main() # call main function