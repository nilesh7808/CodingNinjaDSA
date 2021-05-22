def sortedSquares(nums):
    # arr = []
    # for i in range(0,len(nums)):
    #
    #     arr.append(nums[i] ** 2)
    #     arr.sort()
    #
    # return arr
    x = [num**2 for num in nums]
    i = 0
    j = len(x)-1

    while i<j:

        if x[i] < x[j]:
            j -= 1

        elif x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1

    for i in range(0,len(x)):
        return x

nums = [11, -4, -1, 0, 3, 10]
print(sortedSquares(nums))