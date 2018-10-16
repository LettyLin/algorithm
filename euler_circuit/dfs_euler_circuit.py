import numpy as np


def load_graph(filename):
    file = open(filename)
    info = file.readline().split('\t')
    vertex_num = int(info[0])
    edges_num = int(info[1])
    edges = np.zeros((vertex_num, vertex_num))

    for i in range(edges_num):
        vertex = file.readline().strip().split('\t')
        edges[int(vertex[0])-1, int(vertex[1])-1] = 1
        edges[int(vertex[1])-1, int(vertex[0])-1] = 1

    return edges


def dfs(pos, edges, ):
    pass


e = load_graph('graph.txt')

