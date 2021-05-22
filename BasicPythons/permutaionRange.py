from itertools import product
def tup_sum(n):
    sum =0
    for i in range(len(n)):
        sum=sum+int(n[i])
        return sum
l,h=map(int,input().split())
k=int(input())
arr=[]
for i in range(l,h+1):
    arr.append(str(i))
count=0
p=product(arr,repeat=k)
for i in p:
    if(tup_sum(i)%2==0):
        count=count+1
print(count%1000000007)



# def EvenOdd(low, high):
#     pass
#     from itertools import permutations
#     x=permutations(low,high)
#
#
# low,high=map(int, input().split())
# K=int(input())
