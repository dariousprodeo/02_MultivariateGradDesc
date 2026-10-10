from main import *
from settings import *
from test import testing

def run():

    # Condition on testing params
    if IS_TESTING:
        testing_params = testing()

        feats_num = testing_params[0]
        step_size = testing_params[1]
        maxIt = testing_params[2]

        dataset_instances = testing_params[3]
        labels = testing_params[4]
        starting_point = testing_params[5]
        dataset_dim = testing_params[6]

        b = testing_params[7]

        print("Number of features: ",feats_num)
        print("Dataset dimension: ", dataset_dim)

        if GRADIENT_METHOD == "stochastic":
            return stochastic(feats_num, step_size, maxIt, dataset_instances, labels, starting_point, dataset_dim)

        elif GRADIENT_METHOD == "batch":
            return gradDesc(feats_num, step_size, maxIt, dataset_instances, labels, starting_point, dataset_dim)

        elif GRADIENT_METHOD == "mini-batch":
            return mini_batch(feats_num, step_size, maxIt, dataset_instances, labels, starting_point, dataset_dim, b)

if __name__ == "__main__":
    run()