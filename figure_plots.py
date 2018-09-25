import matplotlib.pyplot as plt
import numpy as np


# scatter_plots
def scatter_plots():
    n = 1024
    # np.random.normal(average, standard_deviation, length)
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)
    # create a window called Figure1
    plt.figure(1)
    # subplot(rows, cols, now)
    plt.subplot(211)
    plt.scatter(X, Y, c=T, alpha=.5)
    # define the limitation of axis
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    plt.subplot(212)
    X2 = np.arange(-5, 5, 0.02)
    Y2 = np.sin(X2)
    plt.plot(X2, Y2)
    plt.show()


scatter_plots()