#Função Map - Pega uma função e aplica a todos os elementos de uma lista

def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]

valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)