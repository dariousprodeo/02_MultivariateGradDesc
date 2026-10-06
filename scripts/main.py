import numpy as np

def gradDesc(feats_num, stepSize, maxIt, count, dataset, starting_point, dataset_dimension):

    # NOTE: dataset[0] = instances, dataset[1] = labels

    # Initializing column vector
    theta = starting_point
    print("Starting point:\n",theta)

    # Initializing the next column vector
    theta_next = np.ones((feats_num,1))

    # Labels
    labels = dataset[1]

    # Summation column vector
    inner_sum = dataset[0] @ theta - labels

    # Initializing partial derivatives column vector
    pds = np.zeros((feats_num,1))
    print("Dataset\n", dataset[0])
    print("Inner sum\n", inner_sum)

    pds = dataset[0].T @ inner_sum
    
    print("Partial derivatives",pds)