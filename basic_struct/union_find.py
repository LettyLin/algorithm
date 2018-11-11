def find(x, p):
    y = x
    while p[y] != 0:
        y = p[y]
    root = y
    y = x
    # 路径压缩
    while p[y]!=0:
        w = p[y]
        p[y] = root
        y = w
    return root


def union(x, y, rank, p):
    u = find(x, p)
    v = find(y, p)
    if rank[u] <= rank[v]:
        p[u] = v
        if rank[u] == rank[v]:
            rank[v] = rank[v]+1
    else:
        p[v] = u


p = [0, 0, 0,0,0,0,0,0,0]
rank = [0, 0, 0,0,0,0,0,0,0]
union(0, 1,rank, p)
union(2,3,rank, p)
union(4,5,rank,p)
union(6,7,rank, p)
union(1,3,rank,p)
union(7, 8,rank, p)
union(5,7,rank,p)
find(4, p)
union(3, 7, rank, p)
find(0, p)
print(p)
print(rank)