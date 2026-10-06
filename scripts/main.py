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

    # Summation column vector
    inner_sum = dataset[0] @ theta - labels

    # Initializing partial derivatives column vector
    pds = np.zeros((feats_num,1))
    print("Dataset", dataset[0])
    print("Inner sum", inner_sum)

    for j in range(feats_num):
        for i in range(dataset_dimension):

            pds[j] += dataset[0][i] * inner_sum[i]

    print("Partial derivatives",pds)