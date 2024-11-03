import string
import random

class PasswordGenerator():
    def __init__(self,length=None,use_uppercase=None,use_chars=None,use_numbers=None) -> None:
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_chars = use_chars
        self.use_numbers = use_numbers

    def generate(self):
        initial_pool = string.ascii_lowercase

        if self.use_uppercase:
            initial_pool += string.ascii_uppercase
        if self.use_numbers:
            initial_pool += string.digits
        if self.use_chars:
            initial_pool += string.punctuation

        password = ''.join(random.choices(initial_pool, k=self.length))

        return password
    
    def run(self):
        # Interfaz básica para el usuario
        print("Configuración del generador de contraseñas:")
        self.length = int(input("Longitud de la contraseña: "))
        self.use_uppercase = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
        self.use_numbers = input("¿Incluir números? (s/n): ").lower() == 's'
        self.use_special_chars = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

        # Genera y muestra la contraseña generada
        password = self.generate()
        print(f"Contraseña generada: {password}")

if __name__ == "__main__":
    generator = PasswordGenerator()  # Crear una instancia del generador
    generator.run()  # Ejecutar la interfaz para generar la contraseña
        