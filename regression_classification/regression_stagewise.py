import numpy as np


def load_data(filename):
    data = []
    label = []
    n = len(open(filename).readline().split('\t')) - 1

    for line in open(filename).readlines():
        temp = []
        split_line = line.split('\t')
        for i in range(n):
            temp.append(float(split_line[i]))
        data.append(temp)
        label.append(float(split_line[-1]))

    return data, label


def stage_wise(x_arr, y_arr, eps=0.01, num_iter=100):
    # regularize data & label: average : 0; variance: 1
    x_mat = np.matrix(x_arr)
    y_mat = np.matrix(y_arr).T
    y_mean = np.mean(y_mat, 0)
    y_mat = y_mat - y_mean
    x_mean = np.mean(x_mat, 0)
    x_var = np.var(x_mat, 0)
    x_mat = (x_mat - x_mean)/x_var

    m, n = np.shape(x_mat)
    ws = np.zeros((n, 1))
    ws_best = ws.copy()
    return_mat = np.zeros((num_iter, n))
    for i in range(num_iter):
        lowest_error = np.inf
        for j in range(n):
            for sign in [-1, 1]:
                ws_new = ws.copy()
                ws_new[j] += eps * sign

                # calculate error of new ws
                y_hat = np.dot(x_mat, ws_new)
                diff = y_hat - y_mat
                error = np.dot(diff.T, diff)

                if error < lowest_error:
                    lowest_error = error
                    ws_best = ws_new

        ws = ws_best.copy()
        return_mat[i, :] = ws.T

    return return_mat


x_arr, y_arr = load_data('abalone.txt')
m = stage_wise(x_arr, y_arr, 0.001, 5000)
print(m)

