class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    # actions
    def reduce_stock(self, amount):
        self.stock -= amount

    def __str__(self):
        return f"{self.name}: --- ${self.price} --- {self.stock}."