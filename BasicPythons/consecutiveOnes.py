nums = [1,1,0,1,1,1]
res = ""
for i in nums:
    res = res + str(i)
l = res.split('0')
#print(l)
print(len(max(l)))