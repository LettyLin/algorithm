import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    n = len(open(filename).readline().split('\t'))
    data = []
    for line in open(filename).readlines():
        split_line = line.strip().split('\t')
        temp_list = []
        for i in range(n):
            temp_list.append(float(split_line[i]))
        data.append(temp_list)

    return data


def distance(point_a, point_b):
    return np.sum(np.power(point_a - point_b, 2))


def rand_center(data_mat, k):
    n = np.shape(data_mat)[1]
    center_point = np.zeros((k, n))
    for i in range(n):
        min_col = np.min(data_mat[:, i])
        max_col = np.max(data_mat[:, i])
        range_col = max_col - min_col
        # cannot np.random.rand(k,1) error: cannot broadcast from (m,1) to (m)
        center_point[:, i] = min_col + range_col*np.random.rand(k).T

    return center_point


def k_means(data_mat, k):
    m = np.shape(data_mat)[0]
    center = rand_center(data_mat, k)
    cluster_allocate = np.zeros((m, 2))
    cluster_moved = True

    while cluster_moved:
        cluster_moved = False
        for i in range(m):
            min_dist = np.inf
            min_index = -1
            for j in range(k):
                dist = distance(data_mat[i, :], center[j, :])
                if dist < min_dist:
                    min_dist = dist
                    min_index = j
            if cluster_allocate[i][0] != min_index:
                cluster_moved = True
            cluster_allocate[i][0] = min_index
            cluster_allocate[i][1] = min_dist

        # recalculate center
        for i in range(k):
            data = data_mat[np.nonzero(cluster_allocate[:, 0] == i)[0]]
            center[i, :] = np.mean(data, 0)

    return center, cluster_allocate

'''
data = load_data('testSet.txt')
data_mat = np.matrix(data)

c, allo = k_means(data_mat, 4)
print(c)

plt.figure(1)
markers = ['o', 'v', 's', '*']
for i in range(4):
    m = data_mat[np.nonzero(allo[:,0]==i)[0]]
    plt.scatter(m[:, 0].tolist(), m[:, 1].tolist(), marker=markers[i])
plt.scatter(c[:,0].tolist(), c[:,1].tolist(), marker='+')
plt.show()
'''