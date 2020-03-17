minha_lista1 = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1, 2, 3, 4, 5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

for item in minha_lista1: # Printar a lista toda.
    print(item)
print("\n")

tamanho = len(minha_lista1) # Tamanho da lista.
print("Tamanho:", tamanho)
print("\n")

minha_lista1.append("limão") # Adicionando itens a lista.
print(minha_lista1)
print("\n")

del minha_lista1[2:] # Remove os itens do range que você quiser.
print(minha_lista1)
print("\n")

del minha_lista1[:] # Remove a lista toda
print(minha_lista1)
print("\n")

lista = [500, 2343, 645, 7, 564, 234, 756757, 0, 9, 53]

lista.sort() # Altera e ordena a lista em ordem crescente
print(lista)
print("\n")

listas = sorted(lista) # Retorna uma lista ordenada
print(listas)
print("\n")

lista.sort(reverse = True) # Ordernar de forma decrescente
print(lista)
print("\n")

lista.reverse() # Reverte a lista
print(lista)
print("\n")

lista2 = ["Sehun", "Kai", "Taeyeon"] # Ordena em ordem alfabética
lista2.sort()
print(lista2)