import numpy as np

features_ls = [10,20,30,40,50]

def normalised_list (l):
    min_ele = np.min(l)
    max_ele = np.max(l)

    n_list = []
    for x in l:
        res = (x - min_ele) / (max_ele - min_ele)
        n_list.append(res)

    return n_list

print(normalised_list(features_ls))