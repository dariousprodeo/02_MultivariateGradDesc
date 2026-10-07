# Importing exec script
from exec import *

# Importing dataset
from dataset import *

# Importing test script
from test import testing

# Bool to fixed params
isTesting_params = True

count = 0

# Condition on testing parameters
if isTesting_params:

    testing_params = testing()

    feats_num_test = testing_params[0]
    step_size_test = testing_params[1]
    max_it_test = testing_params[2]

# Passing feature number to synthetic dataset
    dt = dataset(testing_params[0])

    dataset_instances_test = testing_params[3]
    labels_test = testing_params[4]
    starting_point_test = testing_params[5]

# Passing testing params to exec
    exec(feats_num_test, step_size_test, max_it_test, count, dt, dataset_dimension())

else:
# Number of features
    feats_num = int(input("Enter the number of features: "))
    if feats_num <= 0:
        raise ValueError("Number of features should be a positive integer")

    # Passing feature number to synthetic dataset
    dt = dataset(feats_num)

# Step size (alpha)
    stepSize = input("Enter the step size: ")
    if feats_num <= 0:
        raise ValueError("Step size should be a positive integer")

# Maximum iterations
    maxIt = int(input("Enter maximum iterations: "))
    if maxIt <= 0:
        raise ValueError("Maximum iteration should be a positive integer")

# Passing to exec
    exec(feats_num, stepSize, maxIt, count, dt, dataset_dimension())
