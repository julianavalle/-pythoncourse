import math

# 1. Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade.\n")

elif idade <= 0 or idade > 100:
    print("Idade inválida.\n")

else:
    print("Menor de idade.\n")

# 2. Faça um programa que receba duas notas digitadas pelo usuário. 
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   
nota = int(input("Digite sua nota: "))

if nota >= 6:
    print("Aprovado!\n")

elif nota < 0 or nota > 10:
    print("Nota inválida.\n")

else:
    print("Reprovado.\n")

# 3. Escreva um programa que resolva uma equação de segundo grau.   
def delta(a, b, c):
    return b**2 - 4 * a * c

def raizes(a, b, c):
    if delta(a, b, c) == 0:
        r1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        return print("Essa equação possui apenas uma raiz e é: ", r1)

    elif delta(a, b, c) < 0:
        return print("Essa equação não possui raiz.")
    
    else:
        r1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        r2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
        return print("Valor da primeira raiz: ", r1, "\nValor da segunda raiz: ", r2)

a = int(input("Digite seu a: "))
b = int(input("Digite seu b: "))
c = int(input("Digite seu c: "))
delta(a, b, c)
raizes(a, b, c)
print("\n")

# 4. Escreva um programa que ordene uma lista numérica com três elementos.  
lista1 = []

print("Entre com 3 números!")
for i in range(0, 3):
    print("Digite o", i+1, "número.")
    numeros = int(input())
    lista1.append(numeros)

lista1.sort()
print("Sua lista ordenada é:", lista1)
print("\n")

# 5. Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   
print("Digite a operação que você deseja fazer com 2 números.")
n1 = int(input("Digite o primeiro número: "))
operador = input("Digite o operador: ")
n2 = int(input("Digite o segundo número: "))

if operador == "+":
    op = n1 + n2

if operador == "-":
    op = n1 - n2

if operador == "*":
    op = n1 * n2

if operador == "/":
    op = n1 / n2
    
print("O resultado dessa operação é: ", op)

