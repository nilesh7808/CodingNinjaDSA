
def secondLargest(arr):
    first = -1
    second = -1
    for i in range(0,len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] != first and arr[i] > second:
            second = arr[i]
    print(second)
arr = list(int (i) for i in input().split())
secondLargest(arr)