from main import *
import numpy as np
import random

def exec(feats_num, stepSize, maxIt, count, dataset):
    print("Number of features: ",feats_num)

    # Fixed and non-fixed option to get the starting point
    fixed = True

    # Initializing starting point
    starting_point = np.ones((1,feats_num))

    if fixed:

        # Starting point for loop
        for i in range(feats_num):

            # Assigning values to the row vector
            starting_point[0,i] = random.uniform(-2,2)

        # Calling the algorithm
        gradDesc(feats_num, stepSize, maxIt, count, dataset,starting_point)
        return

    else:
        for i in range(feats_num):
            tmp = float(input("Enter the coordinate corresponding to i = ", i))
            starting_point[0,i] = tmp

            # Calling the algorithm
            gradDesc(feats_num, stepSize, maxIt, count, dataset, starting_point)
            return