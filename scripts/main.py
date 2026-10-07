import numpy as np

def gradDesc(feats_num, step_size, maxIt, count, dataset_instances, labels, starting_point, dataset_dimension):

    # NOTE: dataset[0] = instances, dataset[1] = labels

    # Initializing column vector theta(k)
    theta = starting_point

    # Summation column vector
    inner_sum = dataset_instances @ theta - labels

    # Initializing partial derivatives column vector
    pds = np.zeros((feats_num + 1, 1))
    pds = (dataset_instances.T @ inner_sum) / dataset_dimension

    # First iteration theta(k + 1) for computing the error
    theta_next = theta - step_size * pds

    err = np.linalg.norm(theta - theta_next)

    # TODO: another parameter needed for tolerance
    while err > 1e-6 and count < maxIt:
        theta = theta_next

        inner_sum = dataset_instances @ theta - labels
        pds = (dataset_instances.T @ inner_sum)/dataset_dimension

        theta_next = theta - step_size * pds

        err = np.linalg.norm(theta - theta_next)
        print(f"\nNew point {count}\n", theta_next)
        print(f"\nError {count}\n", err)

        count += 1