import random
import numpy as np

def dataset(feats_num):

    # TODO: Will probably need another params script for the dataset
    dataset_dim = 30

    # Initializing instances
    dataset_instances = np.ones((dataset_dim, feats_num))

    for i in range(dataset_dim):
        for j in range(feats_num):

            if j == 0:
                dataset_instances[i,j] = 1
            else:
                dataset_instances[i,j] = random.uniform(-5,5)
    print(dataset_instances)