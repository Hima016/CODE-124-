def currencyCalculator(AmountINR,curr):
    if curr=="Euro":
        print(AmountINR*0.01417)
    elif(curr=="Britidh Pound"):
        print(AmountINR*0.0100)
    elif(curr=="Australian Dolar"):
        print(AmountINR*0.02140)
    elif(curr=="Canadaian Dollar"):
        print(AmountINR*0.02027)
    else:
        print(-1)

# currencyCalculator(300,"Euro")
# currencyCalculator(300,"Britidh Pound")
# currencyCalculator(300,"Australian Dolar")
# currencyCalculator(300,"Canadaian Dollar")
n=int(input())
a=input()
print(currencyCalculator(n,a))