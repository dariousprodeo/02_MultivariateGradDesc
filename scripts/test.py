import numpy as np
from exec import *

def testing():

    feats_num_test = 2
    stepSize_test = 0.1
    dataset_instances_test = np.array([[1,1,1],[1,2,3],[1,7,1],[1,-1,-3]])
    labels_test = np.array([[3],[14],[51],[11]])

    # Column vectore theta
    starting_point_test = np.ones([feats_num_test + 1,1])
    dataset_dimension_test = 4

    return feats_num_test, stepSize_test, dataset_instances_test, labels_test, starting_point_test