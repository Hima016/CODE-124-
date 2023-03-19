def fun(n):
    for i in str(n):
        if i not in str(double):
            return False
            break
        else:
            continue
    return True
a=int(input())
double=2*a
if len(str(a))==len(str(double)) and fun(a)==True:
    print(True)
else:
    print(False)
