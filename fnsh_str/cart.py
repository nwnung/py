class Cart:
    def __init__(self):
        self.my_products = {}

    # cart actions
    def show_cart(self):
        if not self.my_products:
            print("empty cart")
        else:
            print("Your product list:")
            for product, details in self.my_products.items():
                print(f"{details['product'].name}: {details['amount']} Units - ${details['product'].price * details['amount']}")

    def add_product_cart(self,product,amount):
        if product.stock >= amount:
            if product in self.my_products:
                self.my_products[product]['amount'] += amount
            else:
                self.my_products[product] = {'product': product, 'amount': amount}

            product.reduce_stock(amount)
        else:
            print(f"Not enough stock on product: {product.name} Avialable: {product.stock}")

    def calc_total(self):
        total = sum(item['product'].price * item['amount'] for item in self.my_products.values())
        return total
    
    def empty_cart(self):
        self.my_products = {}