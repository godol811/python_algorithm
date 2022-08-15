# 부품 찾기
import sys


def search(part_array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if part_array[mid] == target:
        return mid

    elif part_array[mid] > target:
        return search(part_array, target, start, mid - 1)

    else:
        return search(part_array, target, mid + 1, end)


n = int(sys.stdin.readline().rstrip())
part = list(map(int, sys.stdin.readline().rstrip().split()))
part.sort()

m = int(sys.stdin.readline().rstrip())
orders = list(map(int, sys.stdin.readline().rstrip().split()))
orders.sort()

check = []

for order in orders:
    result = search(part, order, 0, n - 1)
    if result == None:
        check.append("no")
    else:
        check.append("yes")

for i in check:
    print(i, end=' ')