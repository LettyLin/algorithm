import  numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    data = []
    for line in open(filename).readlines():
        split_line = line.strip().split('\t')
        temp = []
        for i in range(2):
            temp.append(float(split_line[i]))
        data.append(temp)

    return np.matrix(data)


def diff(point_a, point_b):
    return np.sum(np.power(point_a - point_b, 2))


def center_init(data, k):
    n = np.shape(data)[1]
    center = np.zeros((k, n))
    for i in range(n):
        #  = (2, 1)
        min_data = min(data[:, i])
        span = max(data[:, i]) - min_data
        center[:, i] = min_data + span*np.random.rand(k)

    return center


def k_means(data, k):
    m = np.shape(data)[0]
    center = center_init(data, k)
    cluster_allocate = np.zeros((m, 2))

    cluster_changed = True

    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_diff = np.inf
            index = -1
            for j in range(k):
                cur_diff = diff(data[i, :], center[j, :])
                if cur_diff < min_diff:
                    min_diff = cur_diff
                    index = j
            if index != cluster_allocate[i, 0]:
                cluster_changed = True
            cluster_allocate[i, 0] = index
            cluster_allocate[i, 1] = min_diff

        for i in range(k):
            center[i, :] = np.mean(data[np.nonzero(cluster_allocate[:,0]==i)[0]], axis=0)

    return center, cluster_allocate


d = load_data('testSet.txt')
c, a = k_means(d, 4)
plt.figure(1)
plt.scatter(d[:, 0].tolist(), d[:, 1].tolist())
plt.scatter(c[:, 0].tolist(), c[:, 1].tolist(), marker='+')
plt.show()