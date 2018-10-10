import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    n = len(open(filename).readline().split('\t')) - 1
    data = []
    label = []
    for line in open(filename).readlines():
        split_line = line.strip().split('\t')
        temp = []
        for i in range(n):
            temp.append(float(split_line[i]))
        data.append(temp)
        label.append(float(split_line[-1]))

    return data, label


def ridge_regression(data, label, lam=0.2):
    XTX = np.dot(data.T, data)
    ridge_penalty = XTX + np.multiply(np.eye(np.shape(data)[1]), lam)
    if np.linalg.det(ridge_penalty) == 0.0:
        print('cannot do inverse')
        return
    w_hat = np.dot(np.dot(ridge_penalty.I, data.T), label.T)
    return w_hat


def ridge_test(data, label):
    x_mat = np.matrix(data)
    y_mat = np.matrix(label)
    y_mean = np.mean(y_mat, 0)
    y_mat = y_mat - y_mean
    x_mean = np.mean(x_mat, 0)
    x_var = np.var(x_mat, 0)
    x_mat = (x_mat - x_mean) / x_var

    num_lam = 30
    w_mat = np.zeros((num_lam, np.shape(x_mat)[1]))
    for i in range(num_lam):
        w_hat = ridge_regression(x_mat, y_mat, np.exp(i-10))
        w_mat[i, :] = w_hat.T

    return w_mat


data, label = load_data('abalone.txt')
ws = ridge_test(data, label)
# if want to choose the best lam, you need to do cross-validation
