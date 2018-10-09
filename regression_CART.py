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
    mat0 = data[np.nonzero(data[:, feature] > value)[0], :]
    mat1 = data[np.nonzero(data[:, feature] <= value)[0], :]

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
    for feat_index in range(n-1):
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


def is_tree(obj):
    return (type(obj).__name__ == 'dict')


def get_mean(tree):
    if is_tree(tree['right']): tree['right'] = get_mean(tree['right'])
    if is_tree(tree['left']): tree['left'] = get_mean(tree['left'])
    return (tree['left'] + tree['right']) / 2.0


def prune(tree, test_data):
    if np.shape(test_data)[0] == 0:
        return get_mean(tree)

    if is_tree(tree['right']) or is_tree(tree['left']):
        l_set, r_set = split_data(test_data, tree['split_index'], tree['split_value'])
    if is_tree(tree['left']): tree['left'] = prune(tree['left'], l_set)
    if is_tree(tree['right']): tree['right'] = prune(tree['right'], r_set)
    if not is_tree(tree['left']) and not is_tree(tree['right']):
        l_set, r_set = split_data(test_data, tree['split_index'], tree['split_value'])
        error_no_merge = np.sum(np.power(l_set[:, -1] - tree['left'], 2)) + np.sum(np.power(r_set[:, -1] - tree['right'], 2))
        tree_mean = (tree['left'] + tree['right']) / 2.0
        error_merge = np.sum(np.power(test_data[:, -1] - tree_mean, 2))
        if error_merge < error_no_merge:
            print("merging")
            return tree_mean
        else:
            return tree
    else:
        return tree

'''
my_data = load_data('ex2.txt')
my_mat = np.matrix(my_data)
my_tree = create_tree(my_mat, ops=(0, 1))
my_data_test = load_data('ex2test.txt')
my_mat_test = np.matrix(my_data_test)
# pruning tree
tree = prune(my_tree, my_mat_test)

print(tree)
'''

def linear_solve(data_set):
    m, n = np.shape(data_set)
    X = np.matrix(np.ones((m, n)))
    Y = np.matrix(np.ones((m, 1)))
    X[:, 1:n] = data_set[:, 0:n-1]
    Y = data_set[:, -1]
    XTX = np.dot(X.T, X)
    if np.linalg.det(XTX) == 0.0:
        print("cannot do inverse")
        return
    ws = np.dot(XTX.I, np.dot(X.T, Y))
    return ws, X, Y


def model_leaf(data_set):
    ws, X, Y = linear_solve(data_set)
    return ws


def model_err(data_set):
    ws, X, Y = linear_solve(data_set)
    y_hat = np.dot(X, ws)
    return np.sum(np.power(Y - y_hat, 2))


'''
# type of leaf is model or ws, not value
my_mat = np.matrix(load_data('exp2.txt'))
tree = create_tree(my_mat, model_leaf, model_err, (1, 10))
print(tree)
'''


def reg_tree_eval(model, in_dat):
    return float(model)


def model_tree_eval(model, in_dat):
    n = np.shape(in_dat)[1]
    X = np.matrix(np.ones((1, n+1)))
    X[:, 1:n+1] = in_dat
    return float(np.dot(X, model))


def tree_fore_cast(tree, in_data, model_eval=reg_tree_eval):
    if not is_tree(tree):
        return model_eval(tree, in_data)
    if in_data[tree['split_index']] > tree['split_value']:
        if is_tree(tree['left']):
            return tree_fore_cast(tree['left'], in_data, model_eval)
        else:
            return model_eval(tree['left'], in_data)
    else:
        if is_tree(tree['right']):
            return tree_fore_cast(tree['right'], in_data, model_eval)
        else:
            return model_eval(tree['right'], in_data)


def creat_fore_cast(tree, test_data, model_eval=reg_tree_eval):
    m = len(test_data)
    y_hat = np.zeros((m, 1))
    for i in range(m):
        y_hat[i, 0] = tree_fore_cast(tree, np.matrix(test_data[i]), model_eval)
    return y_hat


train_mat = np.matrix(load_data('bikeSpeedVsIq_train.txt'))
test_mat = np.matrix(load_data('bikeSpeedVsIq_test.txt'))

# regression tree
my_tree = create_tree(train_mat, ops=(1, 20))
y_hat = creat_fore_cast(my_tree, test_mat[:, 0])
print(y_hat.T)
print(np.corrcoef(y_hat, test_mat[:, 1], rowvar=0)[0, 1])

# model tree
my_tree = create_tree(train_mat, model_leaf, model_err, ops=(1, 20))
y_hat = creat_fore_cast(my_tree, test_mat[:, 0], model_tree_eval)
print(y_hat.T)
print(test_mat[:, 1].T)
print(np.corrcoef(y_hat, test_mat[:, 1], rowvar=0)[1, 0])

# linear regression 
ws,X,Y = linear_solve(train_mat)
for i in range(np.shape(test_mat)[0]):
    y_hat[i] = test_mat[i, 0]*ws[1, 0]+ws[0,0]
print(np.corrcoef(y_hat, test_mat[:, 1], rowvar=0)[0, 1])
print(y_hat.T)
