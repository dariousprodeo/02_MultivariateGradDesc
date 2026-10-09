import numpy as np
import random

def gradDesc(feats_num, step_size, maxIt, dataset_instances, labels, starting_point, dataset_dimension):

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

    count = 0

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

# Stochastic method
def stochastic(feats_num, step_size, maxIt, dataset_instances, labels, starting_point, dataset_dimension):

    theta = starting_point
    random_instance_index = random.randint(0, dataset_dimension - 1)
    random_instance = dataset_instances[random_instance_index:random_instance_index + 1, :]

    inner_sum = random_instance @ theta - labels[random_instance_index]
    theta_next = theta - step_size * inner_sum * random_instance.T

    err = np.linalg.norm(theta - theta_next)

    count = 0

    while err > 1e-6 and count < maxIt:
        theta = theta_next
        random_instance_index = random.randint(0, dataset_dimension - 1)
        random_instance = dataset_instances[random_instance_index:random_instance_index + 1, :]

        inner_sum = random_instance @ theta - labels[random_instance_index]
        theta_next = theta - step_size * inner_sum * random_instance.T

        err = np.linalg.norm(theta - theta_next)

        print(f"\nNew point {count}\n", theta_next)
        print(f"\nError {count}\n", err)

        count += 1