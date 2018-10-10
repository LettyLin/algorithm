import numpy as np
import matplotlib.pyplot as plt
from unsupervised_learning import k_means


def bi_k_means(datamat, k):
    m = np.shape(datamat)[0]
    center_list = []
    center0 = np.mean(datamat, 0).tolist()
    center_list.append(center0)
    cluster_allocate = np.zeros((m, 2))
    for i in range(m):
        cluster_allocate[i, 1] = k_means.distance(center0, datamat[i, :])

    while len(center_list) < k:
        min_error = np.inf

        # split every cluster
        for i in range(len(center_list)):
            curr_cluster_to_split = datamat[np.nonzero(cluster_allocate[:, 0]==i)[0], :]
            print(np.shape(curr_cluster_to_split))
            curr_cluster_center, curr_cluster_allocate = k_means.k_means(curr_cluster_to_split, 2)
            # total error
            split_error = np.sum(curr_cluster_allocate[:, 1])
            no_split_error = np.sum(cluster_allocate[np.nonzero(cluster_allocate[:, 0]!=i)[0], 1])
            if split_error + no_split_error < min_error:
                min_error = split_error + no_split_error
                center_to_split = i
                split_centers = curr_cluster_center
                split_allocate = curr_cluster_allocate.copy()

        # update the cluster
        # attention this order, 0-class corresponding to len(center_list) but why?
        # if not, bug emerges: valueError:zero-size array. which means curr_cluster_to_split is empty.
        split_allocate[np.nonzero(split_allocate[:, 0] == 1)[0], 0] = len(center_list)
        split_allocate[np.nonzero(split_allocate[:, 0] == 0)[0], 0] = center_to_split

        center_list[center_to_split] = split_centers[0, :]
        center_list.append(split_centers[1, :])
        print('split %d center' % center_to_split)
        print('center_list: ', len(center_list))

        cluster_allocate[np.nonzero(cluster_allocate[:, 0] == center_to_split)[0], :]=split_allocate

    return np.matrix(center_list), cluster_allocate


datamat =np.matrix(k_means.load_data('testSet2.txt'))
center_mat, allo = bi_k_means(datamat, 3)
plt.figure(1)
plt.scatter(datamat[:, 0].tolist(), datamat[:, 1].tolist())
plt.scatter(center_mat[:, 0].tolist(), center_mat[:, 1].tolist(), marker='+')
plt.show()

