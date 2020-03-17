import random
numero = random.randint(0, 10) # Escolhe números aleatórios de 0 a 10
print(numero)

random.seed(1) # Força a selecionar o mesmo número
numero = random.randint(0, 10) # Escolhe números aleatórios de 0 a 10
print(numero)

lista = [6, 45, 9]
numero = random.choice(lista) # Escolhe números aleatórios da lista
print(numero)