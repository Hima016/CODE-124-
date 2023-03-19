list1=[9,3,6,1,5,0,8,2,4,7]
list2=[6,4,6,1,2,2]
result=[]
for i in list2:
    result.append((i,list1.index(i)))
print(result)    
##using LIST COMPREHENSION
print([(i,list1.index(i))for i in list2])
print(dict([(i,list1.index(i))for i in list2]))
###EXtra Method
result4={}
for i in list2:
    result4[i]=list1.index(i)
print(result4)
result4={i:list1.index(i) for i in list2}
print(result4)
