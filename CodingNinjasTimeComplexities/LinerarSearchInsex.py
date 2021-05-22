def linearSearch(arr,x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            print("Entered element is found at index",i)
            break
    else:
        print("No entered element is found")

n = int(input())
arr = list(int(i) for i in input().strip().split())
x = int(input())
linearSearch(arr,x)