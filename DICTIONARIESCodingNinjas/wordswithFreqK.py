# 1st method

s = input("Enter String ")
k = int(input("Enter Frequncy "))
words = s.split()
d = {  }
# for w in words:
#     if w in d:
#         d[w] = d[w] + 1
#     else:
#         d[w] = 1
# or
for w in words:
    d[w] = d.get(w,0) + 1
for w in d:
    if d[w] == k:
        print(w)



# # 2nd method
# def printKFreqWords(s, k):
#     words = s.split()
#     d = {  }
#     for w in words:
#         d[w] = d.get(w, 0) + 1
#     for w in d:
#         if d[w] == k:
#             print(w)
#
# s = input("Enter Statement ")
# k = int(input())
# printKFreqWords(s, k)
