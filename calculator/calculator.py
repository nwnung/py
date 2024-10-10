def calculator(num1, op, num2):
    if not isinstance(num1,(int,float)) or not isinstance(num2,(int, float)):
        return "uno de los numeros no es valido"

    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "no puedes dividir entre 0"

    else:
        return "operacion no valida"

    
op1 = calculator(4,"*",3)
print(op1)