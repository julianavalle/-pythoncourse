# Sem Função Enumerate
lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
    print(i, lista[i])
print("\n")

# Com Função Enumerate

for i, nome in enumerate(lista): #vai retonar um valor i(indíce) e um nome(item)
    print(i, nome)

