import string
import random

class PasswordGenerator:
    def __init__(self,length=12,use_numbers=True,use_special_chars=True,use_uppercase=True):
        self.length = length
        self.use_numbers = use_numbers
        self.use_special_chars = use_special_chars
        self.use_uppercase = use_uppercase

    def configure(self, length, use_uppercase, use_numbers, use_special_chars):
        if length is not None:
            self.length = length
        if use_uppercase is not None:
            self.use_uppercase = use_uppercase
        if use_numbers is not None:
            self.use_numbers = use_numbers
        if use_special_chars is not None:
            self.use_special_chars = use_special_chars

    def generate(self):
        pool = string.ascii_lowercase

        if self.use_numbers:
            pool += string.digits
        if self.use_uppercase:
            pool += string.ascii_uppercase
        if self.use_special_chars:
            pool += string.punctuation

        password = ''.join(random.choices(pool,k=self.length))
        return password

    def init(self):
        length = int(input('Selecciona cuantos caracteres: '))
        numbers = input('Deseas numeros? ').lower() == 's'
        upper = input('Deseas mayusculas? ').lower() == 's'
        special_chars = input('Deseas caracteres especiales?').lower() == 's'

        self.configure(length=length,use_uppercase=upper,use_numbers=numbers,use_special_chars=special_chars)

        password = self.generate()
        print(f'Contraseña generada {password}')


jona = 'nwnung'

if jona == 'nwnung':
    passw = PasswordGenerator()
    passw.init()