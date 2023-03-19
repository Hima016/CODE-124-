mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result1=[]
for i in mat:
    for j in i:
        if j%2!=0:
            result1.append(j**2)
        else:
            result1.append(j**3)
print(result1)
##covert in 2d list
result2=[]
for i in mat:
    result_data=[]
    for j in i:
        if j%2!=0:
            result_data.append(j**2)
        else:
            result_data.append(j**3)
    result2.append(result_data)
print(result2)
##Using LIST COMPREHENSION
print([j**2 if j%2!=0 else j**3 for i in mat for  j in i])##for 1d array
print([[j**2 if j%2!=0 else j**3 for j in i] for  i in mat])####for 2d array