class student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
    def set_details(self,sid,sm,sa):
        self.__student_id=sid
        self.__marks=sm
        self.__age=sa
    def validate_marks(self):
        if 100>=self.__marks>=0:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
        else:
            return True
    def choose_course(self):
        if self.check_qualification():
            self.fees=None
       
class customer:
    def __init__(self,cid,cname,cage,account):
        self.customer_id=cid
        self.customer_name=cname
        self.age=cage
        self.account=account
    def withdraw(self,amount):
        self.amount=amount
        self.temp=self.account.balance-self.amount
        if self.temp<0:
            print("OverdrawException")
        elif self.temp<self.account.min_balance:
            print("moneyLimit is exceed")
        else:
            self.account.balance=self.account.balance-self.amount
            print(f"remaining balance : {self.account.balance}")
            self.take_card()
    def take_card(self):
        print("plese take your card")
    def get_customer_id(self):
        return self.customer_id
    def get_age(self):
        return self.age
    def get_account(self):
        return self.account
class account:
    def __init__(self,account_type,balance,min_balance):
        self.account_type=account_type
        self.balance=balance
        self.min_balance=min_balance
    def get_account_type(self):
        return self.account_type
    def get_balance(self):
        return self.balance
    def get_min_balance(self):
        return self.min_balance
    def set_balance(self,balance):  
        self.balance=balance
class privilegedcustomer(customer):
    def __init__(self,cid,cname,cage,account,bonus):
        self.customer_id=cid
        self.customer_name=cname
        self.age=cage
        self.account=account
        self.bonus_points=bonus
    def withdraw(self,amount):
        self.amount=amount
        self.temp=self.account.balance-self.amount
        if self.temp<0:
            print("OverdrawException")
        elif self.temp<self.account.min_balance:
            print("LimitReachedException")
        else:
            self.account.balance=self.account.balance-self.amount
            print(f"remaining balance : {self.account.balance}")
            super().take_card()
            self.increase_bonus()
    def get_bonus_points(self):
        return self.bonus_points
    def increase_bonus(self):
        if self.account.balance>1000:
            self.bonus_points=self.bonus_points+10
        else:
            self.bonus_points=self.bonus_points+2
        
    
print("----------FIRST ACCOUNT---------")
a1=account("savings",1000,500)
c1=privilegedcustomer(100,"sourav",43,a1,100)
c1.withdraw(200)
print(f"bonus points ={c1.get_bonus_points()}")

print("-------------SECOND ACCOUNT-------")

a2=account("savings",4000,2000)
c2=customer(101,"himanshu",24,a2)
c2.withdraw(3000)

print("--------NEXT PERSON---------")

a3=account("savings",1000,500)
c3=privilegedcustomer(100,"cccc",43,a3,110)
c3.withdraw(2000)
print(f"bonus points ={c3.get_bonus_points()}")