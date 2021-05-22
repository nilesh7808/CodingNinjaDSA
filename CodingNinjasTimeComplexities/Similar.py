arr = [1,5,5,1,4,5]
for i in range(0,len(arr)):
    flag = 0
    for j in range(0,len(arr)):
        if i != j:
            if arr[i] == arr[j]:
                flag = 1
                break
    if flag==0:
        print(arr[i])
    print("Nothing to print")
    break