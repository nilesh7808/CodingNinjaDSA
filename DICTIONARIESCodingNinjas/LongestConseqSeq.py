def LConseqSeq(arr):
    hashMap = {}

    for i in arr:
        if hashMap.get(i):
            continue

        hashMap[i] = 1
        if hashMap.get(i + 1):
            hashMap[i] += hashMap[i + 1]
        while hashMap.get(i - 1):
            hashMap[i - 1] = 1 + hashMap[i]
            i -= 1

    return max(hashMap.itervalues())
arr = list(int (i) for i in input().strip().split())
LConseqSeq(arr)