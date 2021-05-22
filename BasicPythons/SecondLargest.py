def Second_Largest(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print(arr[-2])

arr = [1, 2, 38, 9, 6, 7, 5]
Second_Largest(arr)