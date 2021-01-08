import numpy as np
training_inputs = []
training_inputs2 = []
training_inputs3 = []
training_inputs4 = []
for i in range (3):
    #new = np.random.randint(0,2)
    new = np.random.randint(0,2)
    new2 = np.random.randint(0,2)
    new3 =  np.random.randint(0,2)
    new4 =  np.random.randint(0,2)
    np.append(training_inputs, new)
    np.append(training_inputs2, new2)
    np.append(training_inputs3, new3)
    np.append(training_inputs4, new4)
matrix2 = np.array([[training_inputs, training_inputs2, training_inputs3]]).T
firstOutput = matrix2
print("RANDOM INPUTS: " ,firstOutput)

#why are there no array elements?
