num=int(input())
if(num%3==0 and num%5==0):
    print("multiple of 3 and 5")
if(num%3==0):
    print("multiple of 3")
elif(num%5==0):
    print("multiple of 5")
else:
    print("invalid")