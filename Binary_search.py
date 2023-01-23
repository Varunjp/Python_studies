def binarysearch(lst, key):
    start = 0
    end = len(lst) - 1
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] > key:
            end = mid - 1
        elif lst[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1


lst1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
key = 10
res = binarysearch(lst1, key)
if res == -1:
    print("Not found")
else:
    print("Found at", res)
