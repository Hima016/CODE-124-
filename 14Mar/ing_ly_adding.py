def fun(s):
    if(len(s)<3):
        return s
    elif  'ing' in s[-3:]:
        return s+'ly'
    else:
        return s+'ing'
a=input()
print(fun(a))