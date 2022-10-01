# Henrique Levandoski Richa

# 5. Você tem uma lista de tuplas onde o primeiro campo é o nome de um aluno e o segundo
# sua nota. Crie uma função, usando o Python, C ou C++ 20 e os conceitos de programação
# funcional para criar uma função que ordene listas de tuplas, como a tupla descrita neste
# enunciado. Sem, é claro, usar qualquer função, objeto, ou biblioteca disponíveis na
# linguagem que você escolher.

lista = [('Henrique', 10), ('Adriano', 5), ('Luciana', 7), ('Alex', 9), ('Enzo', 8), ('Frank', 7), ('Frank', 4)]

def ordenaTupla(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i][1] < lista[j][1]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

print(ordenaTupla(lista))