
def sift_up(h, i):
    """
    current element is bigger than its parent, so we need to change
    :param h: the heap array
    :param i: current element index
    :return:
    """
    if i == 1:
        return
    done = False
    while i != 1 and done is False:
        if h[i-1] > h[int(i/2)-1]:
            h[i-1], h[int(i/2)-1] = h[int(i/2)-1], h[i-1]
        else:
            done = True
        i = int(i/2)
    return h


def sift_down(h, i):
    """
    current element is smaller than its child, so we need to change
    :param h: the heap array
    :param i: current element index
    :return:
    """
    n = len(h)
    if 2*i > n:
        return
    done = False
    while 2*i <= n and done is False:
        i = 2 * i
        if i+1<n and h[i]>h[i-1]:
            i = i+1
        if h[int(i/2)-1] < h[i-1]:
            h[int(i/2)-1], h[i-1] = h[i-1], h[int(i/2)-1]
        else:
            done = True

    return h


def insert(h, x):
    h.append(x)
    return sift_up(h, len(h))


def delete(h, i):
    n = len(h)
    x = h[i-1]
    y = h[n-1]
    h.remove(n - 1)
    if i == n:
        return h
    # 删除列表元素
    h[i-1] = y
    if x > y:
        sift_down(h, i)
    else:
        sift_up(h, i)
    return h


def delete_max(h):
    x = h[0]
    delete(h, 1)
    return x


def make_heap(arr):
    for i in range(int(len(arr)/2), 0, -1):
        sift_down(arr, i)


ha = [20, 17, 9, 10, 11, 4, 5, 3, 7, 5]
a = [4, 3, 8, 10, 11, 13, 7, 30, 17, 26]
make_heap(a)
print(a)
