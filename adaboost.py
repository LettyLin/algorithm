import numpy as np


def init_data():
    """
    init data and labels
    :return: data & label
    """
    data = np.matrix([[1.0, 2.1],
                      [1.5, 1.6],
                      [1.3, 1.0],
                      [1.0, 1.0],
                      [2.0, 1.0]])
    label = [1.0, 1.0, -1.0, -1.0, 1.0]
    return data, label


def stump_classify(data, threshold, direc, dimen):
    """
    classifly every dimen of data to get the dimen_label
    :param data:
    :param threshold:
    :param direc: lt or gt
    :param dimen: n dimension
    :return:
    """
    array = np.ones((np.shape(data)[0], 1))
    if direc == 'lt':
        array[data[:, dimen] <= threshold] = -1.0
    else:
        array[data[:, dimen] > threshold] = -1.0
    return array


def create_best_simple_tree(D, data, label):
    """
    choose the best feature to create a decision tree with only one layer
    :return:
    """
    label = np.matrix(label).T
    m, n = np.shape(data)
    steps = 10.0
    min_error = np.inf
    best_stump = {}
    best_predict_labels = np.ones((m, 1))

    # choose feature
    for i in range(n):
        dimen_min = np.min(data[:, i])
        dimen_max = np.max(data[:, i])
        step_size = (dimen_max - dimen_min)/steps
        # choose steps
        for j in range(-1, int(steps)+1):
            # choose direction
            for direc in ['lt', 'gt']:
                threshold = dimen_min+float(j)*step_size
                dimen_label = stump_classify(data, threshold, direc, i)
                error_array = np.ones((m, 1))
                error_array[dimen_label == label] = 0
                weighted_error = np.dot(D.T, error_array)
                # print("dimen: %d;  direc: %s   threshold: \
                #       %.2f;  error: %f" % (i, direc, threshold, weighted_error))

                if weighted_error < min_error:
                    min_error = weighted_error
                    best_stump['dimen'] = i
                    best_stump['threshold'] = threshold
                    best_stump['direc'] = direc
                    best_predict_labels = dimen_label.copy()

    return best_stump, min_error, best_predict_labels


def adaboost(data, label, num_iter=40):
    weak_classifiers = []
    m = data.shape[0]
    D = np.ones((m, 1))/m
    accu_class_est = np.zeros((m, 1))

    for i in range(num_iter):
        best_tree, error, predict_labels = create_best_simple_tree(D, data, label)
        print('D: ', D.T)
        # calculate alpha according to weak the classifier
        alpha = 0.5 * np.log((1-error)/max(error, 1e-16))
        best_tree['alpha'] = alpha
        weak_classifiers.append(best_tree)

        # update D vector
        expon = np.multiply((np.matrix(label).T*(-1)*alpha), predict_labels)
        D = np.multiply(D, np.exp(expon))
        D = D/np.sum(D)

        # accumulate class estimate values
        accu_class_est += np.dot(predict_labels, alpha)
        accu_error = np.multiply(np.sign(accu_class_est) != np.mat(label).T, np.ones((m, 1)))
        accu_error = np.sum(accu_error)/m
        print('class_est: ', predict_labels.T)
        print('accu_class_est: ', accu_class_est.T)
        print('error: ', accu_error)
        print('  ')
        if accu_error == 0.0:
            break

    return weak_classifiers


def ada_classify(data, weak_classifiers):
    data = np.matrix(data)
    m = np.shape(data)[0]
    accu_class = np.zeros((m, 1))
    for i in range(len(weak_classifiers)):
        predice_class = stump_classify(data, weak_classifiers[i]['threshold'], weak_classifiers[i]['direc'], weak_classifiers[i]['dimen'])
        accu_class += predice_class * weak_classifiers[i]['alpha']
        print(accu_class)
    return np.sign(accu_class)


dataset, labels = init_data()
weaks = adaboost(dataset, labels, 10)
d = [1.0, 2.1]
cla = adaboost_classify(d, weaks)
print(cla)