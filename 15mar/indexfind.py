## reference input 3,2,6,5,1,4,8,9 
# l=[i for i in input().split(',')]
# print(l)
# i5=l.index('5')
# i8=l.index('8')
# ans=sum([int(i)for i in l[:i5]+l[i8+1:]])+int("".join(l[i5:i8+1]))
# print(ans)
l=[i for i in input().split(',')]
print(l)
i5=l.index('5')
i8=l.index('8')
ans=sum([int(i)for i in l[:i5]+l[i8+1:]])+int("".join(l[i5:i8+1]))
print(ans)