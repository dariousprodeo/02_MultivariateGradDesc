import numpy as np

def gradDesc(feats_num, stepSize, maxIt, count, dataset, starting_point, dataset_dimension):

    # NOTE: dataset[0] = instances, dataset[1] = labels

    # Initializing column vector
    theta = starting_point
    print(theta)

    # Initializing the next column vector
    theta_next = np.ones((feats_num,1))

    # Labels
    labels = dataset[1]

    # Summation
    inner_sum = dataset[0] @ theta - labels

    # First partial derivative
    first_pd = sum(inner_sum)/dataset_dimension
    print(first_pd)

    # First iteration needed for error condition in the while loop
    for i in range(feats_num):
        theta_next[i,0] = theta[i,0] - stepSize*dataset

    while count < maxIt:

        count += 1
