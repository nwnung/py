class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, amount):
        if self.stock > amount:
            print("reduce stock")
            self.stock -= amount
        else:
            print("invalid amount")

    def __str__(self):
        return f"{self.name} --- ${self.price} --- {self.stock} units"