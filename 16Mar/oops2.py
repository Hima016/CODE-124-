class Mobile:
    def _init_(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*(discount/100)
        print("Total price of",self.brand, "Mobile is",self.total_price)
mob1=Mobile("Apple",200000)
mob2=Mobile("Samsung",100000)
mob1.purchase()
mob2.purchase()