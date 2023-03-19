#For odd number
print([i for i in range(11) if i%2!=0])
#for even number
print([i for i in range(11) if i%2==0])
#For if odd print and print even square
print([i if i%2!=0 else i**2 for i in range(11)])
#-USING SIMPLE FOR LOOP
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2) 
print(result)

