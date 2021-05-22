def subArraySum(arr, n, sum):
    i = 1
    j = i-1
    while i < 1:
        if arr[i] != sum:
            i += 1
            if arr[i] == sum:
                print(j, i,end=" ")
            i += 1
            j += 1
        else:
            print("-1")
n = int(input("Enter Length:"))
arr = list(int (i) for i in input().strip().split())
sum = int(input("Enter sum to do:"))
subArraySum(arr, n, sum)