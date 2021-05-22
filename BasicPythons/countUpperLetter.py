def countUpperLetter(s):
    count = 0
    for i in range(0,len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) < 91:
            count += 1
    print(count)
s = input()
countUpperLetter(s)