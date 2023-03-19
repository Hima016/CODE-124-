result=[array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
# #print(result)
# c=0
# for i in result:
#     if sum(i)%2!=0:
#         c+=1
# print(c)