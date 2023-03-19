def fun(s):
    if(len(s)<2):
        return -1
    else:
        a=s[:2]+s[-2:]
        return a
    
b=input()
print(fun(b))