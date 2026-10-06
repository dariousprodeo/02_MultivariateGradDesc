import numpy as np

def gradDesc(feats_num, stepSize, maxIt, count, dataset, starting_point, dataset_dimension):

    # NOTE: dataset[0] = instances, dataset[1] = labels

    feats_num_test = 2
    stepSize_test = 0.1
    dataset_instances_test = np.array([3,-4])
    labels_test = 3
    starting_point_test = np.ones([feats_num_test,1])
    dataset_dimension_test = 1

    # Initializing column vector
    theta = starting_point_test

    # Initializing the next column vector
    theta_next = np.ones((feats_num_test,1))

    # Summation
    inner_sum = dataset_instances_test @ theta - labels_test
    print("Dataset instances test",dataset_instances_test)
    print("Starting point",theta)
    print(inner_sum)

    # First partial derivative
    first_pd = sum(inner_sum)/dataset_dimension_test
    print("First partial derivative", first_pd)

    # First iteration needed for error condition in the while loop
    for i in range(feats_num):
        theta_next[i,0] = theta[i,0] - stepSize*dataset

    while count < maxIt:

        count += 1
