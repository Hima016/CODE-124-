def matching(m,n):
    for i in m:
        if(i!=' '):
            if(i in n):
                print(i,end='')
a=matching("I like Python"," java is very popular")
print(a)