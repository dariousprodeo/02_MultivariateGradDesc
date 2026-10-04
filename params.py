# Bool to fixed params
isFixed_params = False

# Condition on fixed parameters
if isFixed_params:
    fixed_feats_num = 2
    fixed_stepSize = 0.5
    fixed_maxIt = 200
    count = 0

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