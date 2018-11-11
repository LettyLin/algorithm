import numpy as np


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], a[i] = arr[i], arr[min_index]
    return arr


def selection_sort_regression(arr, i):
    if i < len(arr):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        selection_sort_regression(arr, i+1)


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


def insertion_sort_regression1(arr, i):
    if i > 0 and i < len(arr):
        j = i-1
        x = arr[i]
        while j >= 0 and arr[j]>x:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = x
        insertion_sort_regression1(arr, i+1)


def insertion_sort_regression2(arr, n):
    if n > 0:
        insertion_sort_regression2(arr, n-1)
        x = arr[n]
        j = n-1
        while j>=0 and arr[j] > x:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = x


# 基数排序
def radix_sort(L, k):
    for j in range(1, k+1):
        L10 = []
        for i in range(10):
            L10.append([])
        for i in range(len(L)):
            index_i = int(L[i]/pow(10, j-1))%10
            L10[index_i].append(L[i])
        L = []
        for i in range(0, 10):
            for m in range(len(L10[i])):
                L.append(L10[i][m])
        print(L)
    return L


test = [7467, 1247, 3275, 6792, 9187, 9134, 4675, 1239]
a = [45, 32, 1, 0, 44, 67]
b = [1,5,7,9,2,3,4,6,10]
print(radix_sort(test, 4))

