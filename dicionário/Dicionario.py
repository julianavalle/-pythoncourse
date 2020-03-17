meu_dicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}
print(meu_dicionario["A"])
print("\n")

print(meu_dicionario["B"])
print("\n")

print(meu_dicionario["C"])
print("\n")

print(meu_dicionario)
print("\n")

# Navegação pelo dicionário
for chave in meu_dicionario:
    print(chave + " : " + meu_dicionario[chave])
print("\n")

# Função items
for i in meu_dicionario.items():
    print(i)
print("\n")

# Função Values - Retorna apenas os valores
for i in meu_dicionario.values():
    print(i)
print("\n")

# Função Keys - Navega pelas chaves
for i in meu_dicionario.keys():
    print(i)
print("\n")