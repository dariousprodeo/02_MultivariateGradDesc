from main import *
import numpy as np
import random

def exec(feats_num, step_size, maxIt, count, dataset_instances, labels, starting_point, dataset_dimension, isTesting_params):

    print("Number of features: ",feats_num)
    print("Dataset dimension: ", dataset_dimension)

    if isTesting_params:

        # Calling the algorithm
        gradDesc(feats_num, step_size, maxIt, count, dataset_instances, labels, starting_point, dataset_dimension)
        return

    # Condition on non-testing params
    else:

        # Initializing starting point
        starting_point = np.ones((feats_num + 1, 1))

        for i in range(feats_num):
            tmp = float(input(f"Enter the coordinate corresponding to i = {i}: "))
            starting_point[0,i] = tmp

        # Calling the algorithm
        gradDesc(feats_num, step_size, maxIt, count, dataset,starting_point, dataset_dimension)
        return