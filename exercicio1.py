# Henrique Levandoski Richa

# 1. Usando os conceitos de programação funcional e considerando o universo dos números
# inteiros, implemente a função foldr em Python, C ou C++ 20 tomando como base o
# funcionamento desta função em Haskell. Sem, é claro, usar qualquer função, objeto, ou
# biblioteca disponíveis na linguagem que você escolher.

def foldr(funcao, lista):
    if len(lista) == 0:
        return 0
    else:
        return funcao(lista[0], foldr(funcao, lista[1:]))

def soma(x, y):
    return x + y

print(foldr(soma, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))