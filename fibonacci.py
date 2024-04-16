import unittest

def fibonacci(n):
    if n < 0:
        return 'numero no valido'
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return (fibonacci(n-1) + fibonacci(n-2)) 


if __name__ == "__main__":
    a = int(input('Ingresar un valor: '))   
    print (f'El valor de {a} en la secuencia de fibonacci es {fibonacci(a)}')
