from main import *
import numpy as np
import random
from params import *
from test import testing

def run():

    # Condition on testing params
    if IS_TESTING:
        testing_params = testing()

        feats_num = testing_params[0]
        step_size = testing_params[1]
        maxIt = testing_params[2]

        dataset_instances = testing_params[3]
        labels = testing_params[4]
        starting_point = testing_params[5]
        dataset_dim = testing_params[6]

    print("Number of features: ",feats_num)
    print("Dataset dimension: ", dataset_dim)

    # Calling the algorithm
    return gradDesc(feats_num, step_size, maxIt, dataset_instances, labels, starting_point, dataset_dim)

    # Condition on non-testing params


if __name__ == "__main__":
    run()