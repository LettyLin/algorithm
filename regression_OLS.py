import numpy as np


def load_data(filename):
    data = []
    labels = []
    n = len(open(filename).readline().split('\t')) - 1
    file = open(filename)

    # in the file , x0 = 1.0000
    for line in file.readlines():
        line_data = []
        split_data = line.strip().split('\t')
        for i in range(n):
            line_data.append(float(split_data[i]))
        data.append(line_data)
        labels.append(float(split_data[-1]))

    return data, labels


def regression_OLS(data, labels):
    data_mat = np.matrix(data)
    labels_mat = np.matrix(labels).T
    mat_to_inverse = np.dot(data_mat.T, data_mat)
    if np.linalg.det(mat_to_inverse) == 0.0:
        print('this matrix cannot inverse')
        return
    w = np.dot(mat_to_inverse.I, np.dot(data_mat.T, labels_mat))

    return w


def plot_data(data, labels, w):
    data_mat = np.matrix(data)
    labels_mat = np.matrix(labels)
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data_mat[:, 1].flatten().A[0], labels_mat.T[:, 0].flatten().A[0])
    x_copy = data_mat.copy()
    x_copy.sort(0)
    y_hat = np.dot(x_copy, w)
    ax.plot(x_copy[:, 1], y_hat)
    plt.show()


dataset, labelset = load_data('ex0.txt')
ws = regression_OLS(dataset, labelset)
print(ws)
plot_data(dataset, labelset, ws)