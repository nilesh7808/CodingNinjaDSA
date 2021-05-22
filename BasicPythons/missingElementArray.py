def missingArray(arr, arr1):

    for i in range(0,len(arr)):
        if arr1[i] not in arr:
            print(arr[i])

arr = [1, 2, 3, 4, 5, 6, 7]
arr1 = [1, 2, 3, 4, 5, 8, 9]
missingArray(arr, arr1)