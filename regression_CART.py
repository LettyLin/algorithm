import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    data = []
    n = len(open(filename).readline().split('\t'))
    for line in open(filename).readlines():
        split_line = line.strip().split('\t')
        l = []
        for i in range(n):
            l.append(float(split_line[i]))
        data.append(l)

    return data


def split_data(data, feature, value):
    mat0 = data[np.nonzero(data[:, feature] < value)[0], :]
    mat1 = data[np.nonzero(data[:, feature] >= value)[0], :]

    return mat0, mat1


def reg_leaf(data):
    return np.mean(data[:, -1])


# calculate sum variance
def reg_error(data):
    return np.var(data[:, -1]) * np.shape(data)[0]


def choose_best_feature(data, leaf_type=reg_leaf, err_type=reg_error, ops=(1,4)):
    if len(set(data[:, -1].T.tolist()[0])) == 1:
        return None, leaf_type(data)
    tol_s = ops[0]
    tol_n = ops[1]
    m, n = np.shape(data)
    s = err_type(data)
    best_s = np.inf
    best_index = 0
    best_value = 0
    for feat_index in range(n):
        for val in set(data[:, feat_index].T.tolist()[0]):
            mat0, mat1 = split_data(data, feat_index, val)
            if np.shape(mat0)[0] < tol_n or np.shape(mat1)[0] < tol_n:
                continue
            new_s = err_type(mat0) + err_type(mat1)
            if new_s < best_s:
                best_s = new_s
                best_index = feat_index
                best_value = val

    # if the decrease of error dont bigger than  tol_s
    if (s - best_s) < tol_s:
        return None, leaf_type(data)
    mat0, mat1 = split_data(data, best_index, best_value)
    if (np.shape(mat0)[0] < tol_n) or (np.shape(mat1)[0] < tol_n):
        return None, leaf_type(data)

    return best_index, best_value


def create_tree(data, leaf_type=reg_leaf, err_type=reg_error, ops=(1,4)):
    """

    :param data: dataset to classify
    :param leaf_type: the func to decide the type of leaf of the tree
    :param err_type: the func to calculate error
    :param ops: decide the min-error-decrease and min-class-numbers
    :return: tree (dict
    """
    best_index, best_value = choose_best_feature(data, leaf_type, err_type, ops)
    if best_index == None:
        return best_value
    ret_tree = {}
    ret_tree['split_index'] = best_index
    ret_tree['split_value'] = best_value
    l_set, r_set = split_data(data, best_index, best_value)
    ret_tree['left'] = create_tree(l_set, leaf_type, err_type, ops)
    ret_tree['right'] = create_tree(r_set, leaf_type, err_type, ops)

    return ret_tree


data = load_data('ex00.txt')
data_mat = np.matrix(data)
tree = create_tree(data_mat)
print(tree)