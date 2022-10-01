# Henrique Levandoski Richa

# 2. Usando os conceitos de programação funcional e considerando o universo dos números
# inteiros, implemente a função abs em Python, C ou C++ 20 que devolva o valor absoluto de
# um número dado. Sem, é claro, usar qualquer função, objeto, ou biblioteca disponíveis na
# linguagem que você escolher.

def abs(x):
    if x < 0:
        return -x
    else:
        return x

print(abs(-2))
print(abs(2))