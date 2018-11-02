import numpy as np


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], a[i] = arr[i], arr[min_index]
    return arr


def merge(arr, p, q, r):
    """
    arr[p...q] & arr[q+1...r] has been sorted
    """
    assist = np.zeros(r-p+1)
    s = p
    t = q+1
    k = 0
    while s<=q and t<=r:
        if arr[s] < arr[t]:
            assist[k] = arr[s]
            s = s+1
        else:
            assist[k] = arr[t]
            t = t+1
        k = k+1
    if s == q+1:
        assist[k:r-p+1] = arr[t:r+1]
    else:
        assist[k:r-p+1] = arr[s:q+1]
    return assist


def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur_element = arr[i]
        j = i-1
        while j >=0 and cur_element < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = cur_element
    return arr


a = [45, 32, 1, 0, 44, 67]
b = [1,5,7,9,2,3,4,6,10]
print(insertion_sort(a))

