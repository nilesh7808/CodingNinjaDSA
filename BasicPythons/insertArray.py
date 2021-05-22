def insertArray(arr):
    length = 0
    for i in range(0,3):
        arr[length] = i
        length += 1
    # inserting element into the next place of the previous element(i.e last element insertion), so it will insert element 10 just after 2 and increase length by 1.
    arr[length] = 10
    length += 1

    #insert an element at the first place of an array
    for i in range(3,-1,-1):
        arr[i+1] = arr[i]
    arr[0] = 20

    #insert an element at the middle of an array
    for i in range(4,2,-1):
        arr[i+1] = arr[i]
    arr[3] = 30

    #print all the elements in the array
    for i in range(0, len(arr)):
        print("Index ", i , "contains", arr[i])

arr = [0,0,0,0,0,0,0,0]
insertArray(arr)
