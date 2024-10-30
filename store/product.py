class Product:
    def __init__(self,name,price,stock) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, amount):
        if amount > self.stock:
            print(f'Not enough stock on {self.name}. {self.stock} Avialable')
        else:
            self.stock -= amount

    def __str__(self):
        return f'{self.name} - ${self.price}.'