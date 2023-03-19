class Customer:
    def _init_(self, cust_id, name, age, wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def set_balance(self,amount):
        if amount < 5000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
        print("The balance is", self.wallet_balance)
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Gopal",24000)
print(c1.get_wallet_balance())
c1.set_balance(5000)
print()