def selection_sort(arr):
    for i in range(0,len(arr)):
        min  = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
arr = list(int (i) for i in input().split())
selection_sort(arr)
print(*arr)