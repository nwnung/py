import product
import cart

class Store:
    def __init__(self):
        self.cart = cart.Cart()
        self.store_products = [
            product.Product("Pizza XL", 40, 20),
            product.Product("Pizza LG", 30, 20),
            product.Product("Pizza MD", 20, 20),
            product.Product("Pizza SM", 10, 20),
        ]

    # store actions
    def init(self):
        while True:
            print("\n--- Menú de la Tienda ---")
            print("1. Ver productos")
            print("2. Agregar producto al carrito")     
            print("3. Ver carrito")
            print("4. Finalizar compra")
            print("5. Salir")
            
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.show_products()
            elif opcion == "2":
                self.add_to_cart()
            elif opcion == "3":
                self.cart.show_cart()
            elif opcion == "4":
                self.finish_purchase()
            elif opcion == "5":
                print("Gracias por visitar la tienda.")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
                
    def show_products(self):
        print("Products avialable:")
        for i, product in enumerate(self.store_products, start=1):
            print(f"{i}. {product}")

    def add_to_cart(self):
        self.show_products()
        select = int(input("select number of your product:")) - 1
        if(select < 0 or select >= len(self.store_products)):
            print("Invalid selection")
            return

        select_product = self.store_products[select]
        cuantity = int(input(f"Select amount of {select_product.name}:"))
        self.cart.add_product_cart(select_product, cuantity)

    def finish_purchase(self):
        if not self.cart.my_products:
            print("Your cart is empthy")
            return
        
        total = self.cart.calc_total()
        print(f"Total of your purchase is {total}")
        self.cart.empty_cart()

store = Store()
store.init()