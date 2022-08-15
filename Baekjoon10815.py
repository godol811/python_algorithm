import sys

n = int(sys.stdin.readline().rstrip())
originals = list(map(int, sys.stdin.readline().rstrip().split()))
originals.sort()
m = int(sys.stdin.readline().rstrip())
finds = list(map(int, sys.stdin.readline().rstrip().split()))


def search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return search(array, target, start, mid - 1)
    else:
        return search(array, target, mid + 1, end)


for find in finds:

    if search(originals, find, 0, n - 1) is None:
        print("0", end=' ')
    else:
        print("1", end=' ')
