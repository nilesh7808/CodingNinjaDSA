
def checkRedundant(string):
    l=[]
    for i in range(len(string)):
        if string[i]=="(":
            if i!=len(string)-1 and ( string[i+1]==")"):
                return True
            l.append(string[i])       
        if string[i]==")":
            if len(l)==0:
                return True
            l.pop()                    
    if len(l)==0:
        return False             
    else:
        return True

string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')