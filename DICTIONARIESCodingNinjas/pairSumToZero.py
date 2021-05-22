# def pairSum0(s):
#     pass
#
#
# s = list(int (i) for i in input().strip().split())
# pairSum0(s)

s = input()
words = s.split()
d = {  }
for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1
print(d)