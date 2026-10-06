import numpy as np

def gradDesc(feats_num, stepSize, maxIt, count, dataset, dataset_dimension, starting_point):

    # Initializing column vector
    theta = starting_point

    # Initializing the next column vector
    theta_next = np.ones((feats_num,1))

    # Labels
    labels = dataset[1]

    # Summation
    summation = dataset[0] @ theta - labels
    print(summation)

    # First iteration needed for error condition in the while loop
    for i in range(feats_num):
        theta_next[i,0] = theta[i,0] - stepSize*dataset

    while count < maxIt:

        count += 1
