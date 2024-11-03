import product as Product
import cart as Cart

class Store:
    def __init__(self) -> None:
        self.store_products = [
            Product.Product('Pizza SM',29.9,15),
            Product.Product('Pizza MD',39.9,15),
            Product.Product('Pizza LG',49.9,10),
            Product.Product('Pizza XL',59.9,5),
        ]
        self.cart = Cart.Cart()

    def show_products(self):
        for i, product in enumerate(self.store_products, start=1):
            print(f'{i}. {product.name} - ${product.price}. - Stock: {product.stock}.') 

    def add_product(self,product,amount):
        if product in self.store_products:
            self.cart.add_product(product, amount)
        else:
            print(f"{product.name} no está disponible en la tienda.")

    def my_products(self):
        self.cart.show_cart()

    def finally_purchase(self):
        total = self.cart.calc_total()
        print(f'Total amount is: ${total:.2f}')
        self.cart.empty_cart()
        print('Se vacio tu carrito')

    def init(self):
        while True:
            print('\nWelcome to store')
            print('1. Add product')
            print('2. Delete product')
            print('3. Show products')
            print('4. Show your products')
            print('5. Finally purchase')
            print('6. Exit')

            select = int(input('Select a valid number: '))

            if select == 1:
                self.show_products()
                try:
                    product_index = int(input("Selecciona el número del producto: ")) - 1
                    amount = int(input("Cantidad: "))
                    product = self.store_products[product_index]
                    self.add_product(product, amount)
                except (ValueError, IndexError):
                    print("Entrada no válida, intenta nuevamente.")
            elif select == 2:
                self.cart.show_cart()
                self.cart.delete_product()
            elif select == 3:
                self.show_products()
            elif select == 4:
                self.my_products()
            elif select == 5:
                self.finally_purchase()
            elif select == 6:
                print('Thanks!')
                break


if __name__ == '__main__':
    store = Store()
    store.init()