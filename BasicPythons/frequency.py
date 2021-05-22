arr = ["a", "b", "c","a","a"]
count = 0
for i in range(0,len(arr)):
    if arr[i] == ord(arr[i]):
        count += 1
    print(arr[i])
