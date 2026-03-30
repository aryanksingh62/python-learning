class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self._discount=0
    def __str__(self):
        return f"product is {self.name} and the price ={self.price}"

class Cart:
    def __init__(self):
        self.cart=[]

    def add_item(self,item):
        self.cart.append(item)
        print("item added succesfullly")
    
    def remove_item(self,item):
        if len(self.cart)==0:
            print("cart is empty")
            return
        for i in self.cart:
            if i.name== item:
                self.cart.remove(i)
                print(f"{item} removed")
        print("item not found")
    
    def total_price(self):
        total=0
        for i in self.cart:
            total+= i.price
        return total
    
    def apply_discount(self,percentage):
        t= self.total_price()
        return t-t*percentage/100
    
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self,value):
        if value>=0:
            self._discount=value
        else:
            raise ValueError("discount cannot be negative")
p1 = Product("Shoes", 2000)
p2 = Product("Shirt", 1000)
p3 = Product("Watch", 5000)

cart = Cart()
cart.add_item(p1)
cart.add_item(p2)
cart.add_item(p3)

print(cart.total_price())      
print(cart.apply_discount(10))  
cart.remove_item("Shirt")
print(cart.total_price())      

cart.discount = -10             