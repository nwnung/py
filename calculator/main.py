class Calculator():
    def __init__(self) -> None:
        self.num_one = None
        self.op = None
        self.num_two = None

    # def __str__(self) -> str:
    #     return f'Number one: {self.num_one} OP: {self.op} Number two: {self.num_two}'

    def validate(self):
        if not isinstance(self.num_one, (int,float)) or not isinstance(self.num_two, (int,float)):
            print('invalid operation')
            return

    def calculate(self):
        if self.op == '+':
            print(self.num_one + self.num_two)
        if self.op == '-':
            print(self.num_one - self.num_two)
        if self.op == '*':
            print(self.num_one * self.num_two)
        if self.op == '/':
            print(self.num_one / self.num_two)

            
    def init(self):
        while True:
            print('-- CALCULATOR --')

            number_one = float(input('Select first number: '))
            op = input('Select your operator: ')
            number_two = float(input('Select second number: '))

            self.num_one = number_one
            self.op = op
            self.num_two = number_two

            if self.calculate():
                break

nw = Calculator()
nw.init()