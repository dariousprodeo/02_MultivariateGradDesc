import numpy as np
import random

def gradDesc(feats_num, step_size, maxIt, dataset_instances, labels, starting_point, dataset_dimension):

    # Initializing column vector theta(k)
    theta = starting_point

    # Summation column vector
    error = dataset_instances @ theta - labels

    # Initializing partial derivatives column vector
    pds = np.zeros((feats_num + 1, 1))
    pds = (dataset_instances.T @ error) / dataset_dimension

    # First iteration theta(k + 1) for computing the error
    theta_next = theta - step_size * pds

    err = np.linalg.norm(theta - theta_next)

    count = 0

    # TODO: another parameter needed for tolerance
    while err > 1e-6 and count < maxIt:
        theta = theta_next

        error = dataset_instances @ theta - labels
        pds = (dataset_instances.T @ error)/dataset_dimension

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

    error = random_instance @ theta - labels[random_instance_index]
    theta_next = theta - step_size * error * random_instance.T

    err = np.linalg.norm(theta - theta_next)

    count = 0

    while err > 1e-6 and count < maxIt:
        theta = theta_next
        random_instance_index = random.randint(0, dataset_dimension - 1)
        random_instance = dataset_instances[random_instance_index:random_instance_index + 1, :]

        error = random_instance @ theta - labels[random_instance_index]
        theta_next = theta - step_size * error * random_instance.T

        err = np.linalg.norm(theta - theta_next)

        print(f"\nNew point {count}\n", theta_next)
        print(f"\nError {count}\n", err)

        count += 1

# Mini-batch
def mini_batch(feats_num, step_size, maxIt, dataset_instances, labels, starting_point, dataset_dimension, b):

    theta = starting_point
    dataset_mini_batch = dataset_instances[0 : b, :]

    error = dataset_mini_batch @ theta - labels[0:b]
    theta_next = theta - step_size * dataset_mini_batch.T @ error

    err = np.linalg.norm(theta - theta_next)

    count = 0
    batch_count = 0

    if dataset_dimension % b == 0:
        diff = dataset_dimension - b * (batch_count + 1)

        while err > 1e-6 and count < maxIt:

            theta = theta_next

            if diff > 0:
                dataset_mini_batch = dataset_instances[(batch_count + 1)*b : (batch_count + 2)*b, :]
                error = (dataset_mini_batch @ theta - labels[(batch_count + 1) * b: (batch_count + 2) * b])/b
            else:
                dataset_mini_batch = dataset_instances[0:b,:]
                error = (dataset_mini_batch @ theta - labels[0:b])/b
                batch_count = 0


            theta_next = theta - step_size * dataset_mini_batch.T @ error

            err = np.linalg.norm(theta - theta_next)

            print(f"\nNew point {count}\n", theta_next)
            print(f"\nError {count}\n", err)

            count += 1
            batch_count += 1
            diff = dataset_dimension - b * (batch_count + 1)

    else:
        diff = dataset_dimension -b * (batch_count + 1)

        while err > 1e-6 and count < maxIt:

            theta = theta_next

            if diff > 0:
                dataset_mini_batch = dataset_instances[(batch_count + 1)*b : (batch_count + 2)*b, :]
                error = (dataset_mini_batch @ theta - labels[(batch_count + 1) * b: (batch_count + 2) * b])/b
            else:
                dataset_mini_batch = dataset_instances[0:b,:]
                error = (dataset_mini_batch @ theta - labels[0:b])/b
                batch_count = 0


            theta_next = theta - step_size * dataset_mini_batch.T @ error

            err = np.linalg.norm(theta - theta_next)

            print(f"\nNew point {count}\n", theta_next)
            print(f"\nError {count}\n", err)

            count += 1
            batch_count += 1
            diff = dataset_dimension - b * (batch_count + 1)
