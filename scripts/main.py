import numpy as np

def gradDesc(feats_num, stepSize, maxIt, count, dataset, starting_point, dataset_dimension):

    # Initializing column vector
    theta = starting_point
    print(theta)

    # Initializing the next column vector
    theta_next = np.ones((feats_num,1))

    # First iteration needed for error condition in the while loop
    for i in range(feats_num):
        theta_next[i,0] = theta[i,0] - stepSize*dataset

    while count < maxIt:

        count += 1
