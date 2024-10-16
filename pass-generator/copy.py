import string
import random

class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_special_chars = use_special_chars
    
    def configure(self, length=None, use_uppercase=None, use_numbers=None, use_special_chars=None):
        if length is not None:
            self.length = length
        if use_uppercase is not None:
            self.use_uppercase = use_uppercase
        if use_numbers is not None:
            self.use_numbers = use_numbers
        if use_special_chars is not None:
            self.use_special_chars = use_special_chars
    
    def generate(self):
        # Se encarga de generar la contraseña aleatoria en base a las configuraciones establecidas.
        character_pool = string.ascii_lowercase

        if self.use_uppercase:
            character_pool += string.ascii_uppercase
        if self.use_numbers:
            character_pool += string.digits
        if self.use_special_chars:
            character_pool += string.punctuation

        password = ''.join(random.choices(character_pool, k=self.length))
        
        return password
    
    def run(self):
        # para interactuar con el usuario final
        print("Configuración del generador de contraseñas:")

        length = int(input("Longitud de la contraseña: "))
        use_uppercase = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
        use_numbers = input("¿Incluir números? (s/n): ").lower() == 's'
        use_special_chars = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

        # Llama a configure() para aplicar las configuraciones del usuario
        self.configure(length=length, use_uppercase=use_uppercase, use_numbers=use_numbers, use_special_chars=use_special_chars)

        # Genera y muestra la contraseña generada
        password = self.generate()
        print(f"Contraseña generada: {password}")


if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()