import numpy as np

def gradDesc(feats_num, stepSize, maxIt, count, dataset, starting_point, dataset_dimension):

    # NOTE: dataset[0] = instances, dataset[1] = labels

    # Initializing column vector
    theta = starting_point

    # Initializing the next column vector
    theta_next = np.ones((feats_num,1))

    # Labels
    labels = dataset[1]

    # Summation column vector
    inner_sum = dataset[0] @ theta - labels

    # Initializing partial derivatives column vector
    pds = np.zeros((feats_num,1))

    pds = dataset[0].T @ inner_sum

    # First iteration for error
    theta_next = theta - stepSize * pds

    err = np.linalg.norm(theta - theta_next)

    # TODO: another parameter needed for tolerance
    while err > 1e-6 and count < maxIt:
        theta = theta_next

        inner_sum = dataset[0] @ theta - labels
        pds = dataset[0].T @ inner_sum

        theta_next = theta - stepSize * pds

        err = np.linalg.norm(theta - theta_next)
        print(f"New point {count}\n", theta_next)
        print(f"Error {count}\n", err)

        count += 1