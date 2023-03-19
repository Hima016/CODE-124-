sentences=["a new world record was ser","in the holi city of ayodhya","on the eve of diwali on tuesday","with over three lakh diya or earthen lamps",
           "lit up simultaneously on the banks of sarayu river"]
stopwords=['for','a','of','was','and','to','in','on','with']
# result5=[]
# for i in sentences:
#     row_data=[]
#     for j in i.split():
#         if j not in stopwords:
#             row_data.append(j)
#     result5.append(row_data)
# print(result5)

result1=[]
for i in sentences:
    result2=[]
    for j in i.split():
        if j not in stopwords:
            result2.append(j)
    result1.append(result2)
print(result1)