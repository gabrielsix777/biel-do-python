def calculadora(num1, num2, operação):
# criando as operações e definindo o nome de cada uma
    if operação == 'adição':
        resultado = num1 + num2
    elif operação == 'subtração':
        resultado = num1 - num2
    elif operação == 'multiplicação':
        resultado = num1 * num2
    elif operação == 'divisão':
        resultado = num1 / num2
    
    return resultado

print(calculadora(3,5,'multiplicação'))
print(calculadora(10,5,'subtração'))
print(calculadora(15,3,'divisão'))
print(calculadora(5,5,'adição'))
