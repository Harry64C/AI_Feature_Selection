# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.euclidean.html#scipy.spatial.distance.euclidean
# must run pip install scipy first
from scipy.spatial import distance

class Classifier:
    def __init__(self):
        self = self 

    def train(self, filename = "small-test-dataset.txt"): 
        self.dataVals = {} # dictionary that will hold the data

        file = open(filename, 'r')
        data = file.readlines() # read all lines into a list
        instanceIdx = 0

        for row in data: # parse the row
            row = row.split('\n')
            row = row[0].split('  ')
            row.remove('')

            instance = [int(row[0][0])] # get the instance class

            for i in row[1:]: 
                for j in i.split(): # takes care of any whitespace that got through
                    instance.append(float(j)) # python float() converts IEEE to double automatically

            self.dataVals[instanceIdx] = instance
            instanceIdx += 1

        file.close()

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
    def __init__(self, dataset = "small-test-dataset.txt"):
        self.classifier = Classifier()
        self.classifier.train(dataset)

    def evaluate(self, features = []):
        c = self.classifier
        hits, misses = 0, 0

        for i in range(0, len(c.dataVals)): # calculate accuracy using NN for each
            if c.dataVals[i][0] == c.test(i, features):
                hits += 1
            else:
                misses += 1

        return hits / (hits + misses)




def test():

    inp = input("Enter which features would you like to test: ")
    
    features = []
    for i in inp.split():
        features.append(int(i))

    
    v = Validator("large-test-dataset.txt")
    print("accuracy is", v.evaluate(features))


test()