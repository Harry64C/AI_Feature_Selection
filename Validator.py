# must run pip install scipy first
from scipy.spatial import distance

import numpy as np 
import time

class Classifier:
    def __init__(self):
        self = self 

    def train(self, filename): 
        print("\nStarting training")
        startTime = time.perf_counter()
        
        self.dataVals = {} # dictionary that will hold the data
        self.cols = {}

        file = open(filename, 'r')
        data = file.readlines() # read all lines into a list
        instanceIdx = 0

        for row in data: # parse the row
            col = 0
            
            row = row.split('\n')
            row = row[0].split('  ')
            row.remove('')

            instance = [int(row[0][0])] # get the instance class

            for i in row[1:]: 
                for j in i.split(): # takes care of any whitespace that got through
                    instance.append(float(j)) # python float() converts IEEE to double automatically

                    dataCol = self.cols.get(col, []) # also insert data in columns for later normalization
                    dataCol.append(float(j))
                    self.cols[col] = dataCol
                    col += 1

            self.dataVals[instanceIdx] = instance
            instanceIdx += 1

        file.close()
        print("Training took", time.perf_counter() - startTime, "seconds!\n")


    def normalize(self):
        print("Starting data normalization")
        startTime = time.perf_counter()
        mean = []
        std = []

        for i in self.cols.values():
            # using numpy to easily get the mean and standard deviation for each data column
            mean.append(np.mean(i))
            std.append(np.std(i))

        for i in range(0, len(self.dataVals)):
            row = self.dataVals[i][1:]

            for j in range(0, len(row)):
                #print("row", j, "was", row[j])
                self.dataVals[i][j+1] = (row[j] - mean[j]) / std[j]

        #print(self.dataVals)
        print("Data normalization took", time.perf_counter() - startTime, "seconds!\n")



    def test(self, id, features = []): # returns the expected class of the id
        closest = [float('inf'), -1] # initalize closest point as class -1 with distance of infinity

        i = 0
        while i < len(self.dataVals):

            if (id == i): # leave out self
                i += 1
                continue
            
            instance = self.dataVals[id]
            row = self.dataVals[i]

            if (features == []): # use all features
                row = row[1:]
                instance = instance[1:]

            else: # only include the features passed in
                tempInstance = []
                tempRow = []
                for j in features:
                    tempInstance.append(instance[j])
                    tempRow.append(row[j])

                instance = tempInstance
                row = tempRow

            # library function that returns the euc distance between the current row and the test instance
            eucDist = distance.euclidean(row, instance) 

            if eucDist < closest[0]:
                #print("new closest upon", row)
                closest[0] = eucDist
                closest[1] = self.dataVals[i][0]

            i += 1
        
        return closest[1]
    

class Validator:
    def __init__(self, dataset):
        self.classifier = Classifier()
        self.classifier.train(dataset)
        self.classifier.normalize()

    def evaluate(self, features = []):
        print("Starting accuracy evaluation for feature set", features)
        startTime = time.perf_counter()

        c = self.classifier
        hits, misses = 0, 0

        for i in range(0, len(c.dataVals)): # calculate accuracy using NN for each
            if c.dataVals[i][0] == c.test(i, features):
                hits += 1
            else:
                misses += 1

        print("Accuracy evaluation took", time.perf_counter() - startTime, "seconds!\n")
        return hits / (hits + misses)
        




def test():

    inp = input("Enter which features would you like to test: ")
    
    features = []
    for i in inp.split():
        features.append(int(i))

    filename = input("Enter the filename of the dataset you would like to use: ")
    # large-test-dataset.txt
    v = Validator(filename)

    print("Accuracy for these features is", v.evaluate(features))

# test()