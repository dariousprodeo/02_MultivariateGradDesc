import numpy as np

def testing():

    feats_num_test = 2
    step_size_test = 0.01
    max_it_test = 200
    dataset_instances_test = np.array([[1,1,1],[1,2,3],[1,7,1],[1,-1,-3],[-1,4,2]])
    labels_test = np.array([[3],[14],[51],[11],[22]])

    # Column vector theta(k)
    starting_point_test = np.ones([feats_num_test + 1,1])

    # Given matrix of instances we compute the dimension of the dataset
    dataset_dim_test = dataset_instances_test.shape[0]

    b = 2

    return feats_num_test, step_size_test, max_it_test, dataset_instances_test, labels_test, starting_point_test, dataset_dim_test, b