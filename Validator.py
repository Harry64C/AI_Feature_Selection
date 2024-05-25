
class Validator:
    def __init__(self):
        print("initialized")

    def loadData(self, filename = "large-test-dataset.txt"): # small dataset set as default
        self.dataVals = {} # dictionary that will hold the data

        file = open(filename, 'r')
        data = file.readlines() # read all lines into a list

        for row in data: # parse the row
            row = row.split('\n')
            row = row[0].split('  ')
            row.remove('')

            classVal = int(row[0][0]) # get the instance class

            for i in row[1:]: 
                for j in i.split(): # takes care of any whitespace that got through
                    instances = self.dataVals.get(classVal, [])
                    instances.append(float(j)) # python float() converts IEEE to double automatically
                    self.dataVals[classVal] = instances

        file.close()
        




def test():

    # inp = input("Enter which features would you like to test: ")
    # features = []

    # for i in inp:
    #     features.append(i)

    validate = Validator()
    validate.loadData()

    print(validate.dataVals)

    #print(features)


test()