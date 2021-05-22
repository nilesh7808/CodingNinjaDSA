from math import sqrt
def Distinct_Or_Not(String):
    Total_Chars = 256
    count = [0] * 256
    for i in range(0, len(String)):
        if String[i] != " " :
            count[ord(String[i])] += 1
    c = i
    for i in range(c):
        if count[ord(String[i])] == 1:
            for j in range(2, int(sqrt(len(String)))+1):
                if len(String) % j == 0:
                    return False
            return True
String = input()
if (Distinct_Or_Not(String)):
    print("True")
else:
    print("False")