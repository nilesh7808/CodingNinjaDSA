# using bubble sort algorithm and sorted method of set or tuple

def Second_Largest(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    second_Highest = sorted(set(arr))[-2]
    print(second_Highest)

arr = [1, 2, 38, 9, 38, 7, 5]
Second_Largest(arr)