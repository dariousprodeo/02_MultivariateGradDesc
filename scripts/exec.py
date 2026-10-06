from main import *
import numpy as np
import random

def exec(feats_num, stepSize, maxIt, count, dataset, dataset_dimension):
    print("Number of features: ",feats_num)
    print("Number of features: ", dataset_dimension)
    # Fixed and non-fixed option to get the starting point
    fixed = True

    # Initializing starting point
    starting_point = np.ones((feats_num,1))

    if fixed:

        # Starting point for loop
        for i in range(feats_num):

            # Assigning values to the column vector
            starting_point[i,0] = random.uniform(-2,2)

        # Calling the algorithm
        gradDesc(feats_num, stepSize, maxIt, count, dataset,starting_point, dataset_dimension)
        return

    else:
        for i in range(feats_num):
            tmp = float(input(f"Enter the coordinate corresponding to i = {i}: "))
            starting_point[0,i] = tmp

        # Calling the algorithm
        gradDesc(feats_num, stepSize, maxIt, count, dataset,starting_point, dataset_dimension)
        return