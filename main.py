import numpy as np

def gradDesc(feats_num, stepSize, maxIt, count, dataset,starting_point):

    theta = np.zeros(feats_num)
    print(starting_point)
    print(theta)