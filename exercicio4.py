# Henrique Levandoski Richa

# 4. Usando os conceitos de programação funcional e a linguagem Python, C ou C++ 20 escreva
# uma função que devolva a lista de todos os números de Fibonacci até um valor dado
# considerando que a sequência de Fibonacci começa em zero. Sem, é claro, usar qualquer
# função, objeto, ou biblioteca disponíveis na linguagem que você escolher.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_list(n):
    lista = []
    i=0
    while(i!=n):
        lista.append(fibonacci(i))
        i=i+1
    return lista

print(fibonacci_list(12))