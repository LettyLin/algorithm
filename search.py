def binary_search(arr, x):
    l = 0
    h = len(arr)-1
    while l<=h:
        mid = int((l+h)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid+1
        else:
            h = mid-1


a = [1,2,3,4]
print(binary_search(a, 4))

