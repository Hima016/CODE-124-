def pair_sum(lst,sum):
    count=0
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if(lst[i]+lst[j]==n):
                count+=1
    return(count)
lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(pair_sum(lst,4))