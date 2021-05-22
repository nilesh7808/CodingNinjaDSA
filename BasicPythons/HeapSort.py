from heapq import heappop, heappush
def heap_sort(array):
    heap = []
    for i in array:
        heappush(heap, i)
    HeapSort = []

    while heap is True:
        HeapSort.append(heappop(heap))

    return HeapSort

array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(heap_sort(array))