def highFreq(s):
    words = s.split()
    d = {  }
    for w in words:
        if w in d:
            d[w] = d.get(w, 0) + 1
        else:
            d[w] = 1
    temp = 0
    max = -1
    for w in words:
        if d[w] > max:
            max = d[w]
            temp = w
    return temp
s = input("Enter String:-\n")
print(highFreq(s))