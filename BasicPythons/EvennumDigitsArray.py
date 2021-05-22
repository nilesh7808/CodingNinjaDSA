#input nums
nums = [12, 345, 2, 6, 7896]

#nums[i] = 12 having 2 digits (i.e 1 and 2) so count will be 1 because there are 2 digits i.e even no. of digits
#nums[i] = 345 having 3 digits (i.e 3, 4 and 5) no count because odd number of digits in a number 345(i.e 3,4,5)
#similar for all the elements in an array

#output = number of even digits in nums is 2

newArr = []
count = 0
for i in range(0,len(nums)):
    #typecast all the values in the nums into string and store all that values
    x = str(nums[i])

    #append length of all the values into new array i.e newArr
    newArr.append(len(x))
    # now run all the case for even odd in an array
for j in range(0,len(newArr)):
    if newArr[j] % 2 == 0:
        count += 1

print(count)

# def checkEvens(nums):
#     evens = 0
#     for i in nums:
#         if nums[i] % 2 == 0:
#             evens += 1
#
# def Count(num):
#     count = 0
#     while nums>0:
#         count += 1
#         num = num // 2
#     return count
#
