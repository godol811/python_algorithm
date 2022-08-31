import heapq
def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([2,5,7,5,4,6,0,2,1,1])
print(result.sort(reverse=True))