s=input()
s1=[i for i in s]
s3=input()
s4=[j for j in s3]
str=[]
for i in s1:
    for j in s4:
        if j=='':
            continue
        if i==j:
            str.append(j)
        if j in str:
            continue
        else:
            str.append(j)
for i in str:
    print(i,end='')