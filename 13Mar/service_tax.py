n_adult=int(input("Enter the no of adult: "))
n_childs=int(input("enter number of chile: "))
total=(n_adult*37550.0)+(n_childs*37550.5)/3
print(total)
total1=total*0.27
total2=total+total1
print("with ur service tax",total2)
total_amount=total2*0.90
print("total_amount",total_amount)
##Another way
n_adult=int(input("Enter the no of adult"))
n_childs=int(input("enter number of chile"))
total=((((n_adult*37550.0)+(n_childs*37550.0)/3)*1.07)*0.90)
print(total)