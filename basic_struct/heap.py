def sift_up(h, i):
    # 根节点
    if i == 1:
        return h
    done = False
    while done is False and i > 1:
        if h[i-1] > h[int(i/2)-1]:
            h[i-1], h[int(i/2)-1] = h[int(i/2)-1], h[i-1]
        else:
            done = True
        i = int(i/2)
    return h


def sift_down(h, i):
    # 叶子节点
    if 2*i > len(h):
        return h
    done = False
    while done is False and 2*i <= len(h):
        i = 2*i
        if i<len(h) and h[i-1] < h[i]:
            i = i+1
        if h[i-1] > h[int(i/2)-1]:
            h[i-1], h[int(i/2)-1] = h[int(i/2)-1], h[i-1]
        else:
            done = True
    return h


def insert(h, x):
    h.append(x)
    sift_up(h, len(h))
    return h


def delete(h, i):
    x = h[i-1]
    y = h[len(h)-1]
    del(h[len(h)-1])
    if i == len(h)+1:
        return h
    h[i-1] = y

    if y > x:
        sift_up(h, i)
    else:
        sift_down(h, i)
    return h


# O(n)
def make_heap(arr):
    i = int(len(arr)/2)
    while i > 0:
        sift_down(arr, i)
        i = i-1
    return arr


# 用堆进行排序。首先将数组转化为堆->然后将堆顶即最大值与最后一位交换->shiftdown重新构造堆
# O(nlogn)
def heap_sort(arr):
    arr = make_heap(arr)
    print(arr)
    for j in range(len(arr), 1, -1):
        arr[0], arr[j-1] = arr[j-1], arr[0]
        arr[:j-1] = sift_down(arr[:j-1], 1)
    return arr


ha = [20, 17, 9, 10, 11, 4, 5, 3, 7, 5]
a = [4, 3, 8, 10, 11, 13, 7, 30, 17, 26]
print(heap_sort(a))
