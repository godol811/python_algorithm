import sys

n = int(sys.stdin.readline().rstrip())

index_arr = []
search_arr = []


index_arr = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())

search_arr = list(map(int, sys.stdin.readline().rstrip().split()))

index_arr.sort()


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if target == arr[mid]:
        return mid

    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


for search in search_arr:

    if binary_search(index_arr, search, 0, n - 1) == None:
        print(0, end=' ')
    else:
        print(1, end=' ')
