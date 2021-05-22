# def checkNestingDepth(S):
#     exp = []
#     for i in S:
#         if i in '(':
#             exp.append(i)
#         elif i is ')':
#             if (not exp or exp[-1]):
#                 exp.pop()
#             exp.pop()
#     count = 0
#     for i in range(0,len(S)):
#         if S[i]
# T = int(input())
# for i in range(T):
#     S = input()
#     print(checkNestingDepth(S))
s = input()
x = []
for i in range(0,len(s)):
    if s[i] == '1':
        print("(",s[i],")",end = "")