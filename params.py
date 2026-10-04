# Importing main function
import main
from main import gradDesc

# Importing dataset
from dataset import dataset

# Bool to fixed params
isFixed_params = True

count = 0

# Condition on fixed parameters
if isFixed_params:
    fixed_feats_num = 2
    fixed_stepSize = 0.5
    fixed_maxIt = 200

# Passing params to dataset
    dataset(fixed_feats_num)
# Passing params to alg
    gradDesc(fixed_feats_num, fixed_stepSize, fixed_maxIt, count)
else:
# Number of features
    feats_num = int(input("Enter the number of features: "))
    if feats_num <= 0:
        raise ValueError("Number of features should be a positive integer")

# Step size (alpha)
    stepSize = input("Enter the step size: ")
    if feats_num <= 0:
        raise ValueError("Step size should be a positive integer")

# Maximum iterations
    maxIt = int(input("Enter maximum iterations: "))
    if maxIt <= 0:
        raise ValueError("Maximum iteration should be a positive integer")

# Passing params to dataset
    dataset(feats_num)
# Passing params to alg
    gradDesc(feats_num, stepSize, maxIt, count)