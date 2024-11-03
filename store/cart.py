class Cart:
    def __init__(self) -> None:
        self.my_products = []

    # se le pasa un objecto como parametro product y amount es un numero int
    def add_product(self, product, amount):
        if product.stock >= amount:
            # Busca si el producto ya está en la lista
            for item in self.my_products:
                if item['product'] == product:
                    # Si ya está, aumenta la cantidad
                    item['amount'] += amount
                    break
            else:
                # Si no está, añade el producto como nuevo diccionario
                self.my_products.append({'product': product, 'amount': amount})

            # Reduce el stock del producto en la tienda
            product.reduce_stock(amount)
            print(f"{amount} unidad(es) de {product.name} añadido(s) al carrito.")

            self.calc_total()
        else:
            print(f"No hay suficiente stock de {product.name}. Disponible: {product.stock}")

    def delete_product(self):
        deleted_product = int(input('Select deleted product number: ')) -1

        self.my_products.pop(deleted_product)

    def show_cart(self):
        if len(self.my_products) > 0:
            print("Productos en el carrito:")
            for i,item in enumerate(self.my_products, start=1):
                print(f"{i}. {item['product']} - Amount: {item['amount']}")

        else:
            print('Your cart is empty')


    def calc_total(self):
        total = sum(item['product'].price * item['amount'] for item in self.my_products)
        round(total, 2)
        return total
    
    def empty_cart(self):
        self.my_products = []