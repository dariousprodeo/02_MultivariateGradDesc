import random
import numpy as np

def dataset_dimension():

    # TODO: Will probably need another params script for the dataset
    dataset_dim = 30
    return dataset_dim

def dataset(feats_num):

    dataset_dim = dataset_dimension()

    # Initializing instances
    dataset_instances = np.ones((dataset_dim, feats_num))

    for i in range(dataset_dim):
        for j in range(feats_num):

            if j == 0:
                dataset_instances[i,j] = 1
            else:
                dataset_instances[i,j] = random.uniform(-5,5)

    return dataset_instances