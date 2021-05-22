def rate(n):
    total = 0
    i = 0
    count = 2
    while i < n:
        j = 0
        count += 2
        while j < 10:
            total = i * j + total
            j = j + 1
            count += 3
        count += 2
        i = i + 1
    count += 2
    return count
n = int(input())
print(rate(n))