from queue import PriorityQueue
import copy
import random

def evaluate(Node):
    offset = float(random.randint(0, 9)) / 10
    return random.randint(0, 100) + offset


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
        for i in range(1, featureCnt+1): # may use set because lookup is much faster than a list
            self.fetList.add(i)

    def createFrontier(self, curr): # creates the frontier from curr state and new features
        frontier = []
        if (self.algorithm == 1): # Forward Selection
            for i in self.fetList:
                newFeatures = copy.copy(curr.features)
                newFeatures.append(i)

                temp = Node(newFeatures, 0, i)
                temp.accuracy = evaluate(temp)

                frontier.append(temp)

        elif (self.algorithm == 2): # Backward Elimination
            for i in self.fetList:
                print(i, self.fetList, curr.features)
                newFeatures = copy.copy(curr.features)
                newFeatures.remove(i)

                temp = Node(newFeatures, 0, i)
                temp.accuracy = evaluate(temp)

                frontier.append(temp)
            
        
        return frontier

def printFrontier(frontier): # helper function for output
    for i in frontier:
        print("\n\tUsing feature(s)", i.features, end = " ")
        print ("accuracy is", i.accuracy, "%")


def main():
    
    totalFeatures = int(input("Welcome to Harrison Cooper Feature Selection Algorithm.\nPlease enter total number of features: "))
    algNum = int(input("Type the number of the algorithm you want to run.\n\n\tForward Selection\n\tBackward Elimination\n\tHarrison's Special Algorithm.\n"))

    curr = Node([], 1 / totalFeatures)
    if (algNum == 2):
        for i in range(1, totalFeatures+1):
            curr.features.append(i)

    problem = Problem(totalFeatures, algNum)
    frontier = problem.createFrontier(curr)

    print("initial frontier:")
    printFrontier(frontier)

    print("\nBeginning search.")
    allTimeBest = Node()

    while (problem.fetList): # loop while there are still new features to add
        curr = Node()

        for i in frontier:
            if (i.accuracy > curr.accuracy):
                curr = i

        problem.fetList.remove(curr.newestFet) # remove the chosen feature from featureList

        print("\nFeature set", curr.features, "was best, accuracy is", curr.accuracy, "%")

        if (curr.accuracy < allTimeBest.accuracy):
            print("\n(Warning, Accuracy has decreased!)")
        else: 
            allTimeBest = curr

        frontier = problem.createFrontier(curr)
        printFrontier(frontier)

    print("Finished search!! The best feature subset is", allTimeBest.features, ", which has an accuracy of", allTimeBest.accuracy, "%")
        


if __name__=="__main__": 
    main()