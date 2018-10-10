import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    m = len(open(filename).readline().split('\t')) - 1
    data = []
    label = []
    for line in open(filename).readlines():
        split_line = line.strip().split('\t')
        temp = []
        for i in range(m):
            temp.append(float(split_line[i]))
        data.append(temp)
        label.append(float(split_line[-1]))

    return data, label


def lwlr(test_point, x, y, k=1.0):
    m = np.shape(x)[0]
    weight = np.eye(m)

    for j in range(m):
        diff = x[j] - test_point
        weight[j, j] = np.exp(np.dot(diff, diff.T)/(-2.0*k**2))

    XTWX = np.dot(x.T, np.dot(weight, x))
    if np.linalg.det(XTWX) == 0.0:
        print('cannot reverse')
        return

    w = np.dot(np.dot(np.dot(XTWX.I, x.T), weight), y.T)
    y_hat = np.dot(test_point, w)
    return y_hat


def lwlr_test(test_arr, x, y, k=1.0):
    m = np.shape(test_arr)[0]
    y_hat = np.zeros(m)
    for i in range(m):
        y_hat[i] = lwlr(test_arr[i], x, y, k)

    return y_hat


data, label = load_data('ex0.txt')
x_mat = np.matrix(data)
y_mat = np.matrix(label)

y_hat = lwlr_test(x_mat, x_mat, y_mat, 0.01)
strInd = x_mat[:, 1].argsort(0)
x_sort = x_mat[strInd][:, 0, :]
plt.plot(x_sort[:, 1], y_hat[strInd])
plt.scatter(x_mat[:, 1].flatten().A[0], y_mat.flatten().A[0], s=2, c='red')
plt.show()
