print("Olá Mundo\n")

# ****************************************** VARIÁVEIS ******************************************
var1 = 1 #Variável Inteira
var2 = 1.1 #Variável Float
var3 = "String" #Variável String
var4 = True #Variável Booleana

print(var1, "- Variável Inteira")
print(var2, "- Variável Float")
print(var3, "- Variável String")
print(var4, "- Variável Booleana\n")

# *********************************** ESTRUTURAS CONDICIONAIS ***********************************
x = 1
y = 2

if x == y:
    print("Números iguais\n")
elif x < y:
    print("x menor que y\n")
elif y > x:
    print("y maior que x\n")
else:
    print("Números diferentes\n")

# ********************************* ESTRUTURAS DE REPETIÇÃO: FOR *********************************
lista1 = [1, 3, 5, 7, 9]
lista2 = ["olá", "mundo", "!"]
lista3 = [1, "prato", "de", "trigo", "para", 1, "tigre", "triste", 0.0]

print("Lista 1:")
for i in lista1:
    print(i)
print("\n")

print("Lista 2:")
for i in lista2:
    print(i)
print("\n")

print("Lista 3:")
for i in lista3:
    print(i)
print("\n")

# ******************************** ESTRUTURAS DE REPETIÇÃO: WHILE ********************************
z = 1

while z < 10:
    print(z)
    z += 1
print("\n")

# ***************************** ESTRUTURAS DE REPETIÇÃO: FOR E RANGE *****************************
for i in range(10): #Imprime uma lista com 10 elementos de 0 até 9.
    print(i) 
print("\n")

for i in range(10, 20): #Imprime uma lista de 10 elementos de 10 até 19.
    print(i) 
print("\n")

for i in range(10, 20, 2): #Imprime uma lista de 10 elementos de 10 até 19 de 2 em 2.
    print(i) 
print("\n")

# ******************************************** INPUT ********************************************
numero = input("Digite um número: ") #Input de números
print("O número digitado é:", numero)
print("\n")

nome = input("Digite um nome: ") #Input de string
print("Bem-vindo(a)", nome)
print("\n")

# ******************************** FUNÇÔES STRINGS - CONCATENAÇÃO ********************************
a = "Oh"
b = "Sehun"

concatenar = a + " " + b #Junção de strings
print("Concatenação:", concatenar)
print("\n")

tamanho = len(concatenar)
print("Tamanho da concatenação:", tamanho)
print("\n")

# *************************** FUNÇÔES STRINGS - NAVEGAÇÂO PELO ÍNDICE **************************
print(a[0]) #Imprime a primeira posição da string "a"
print(a[1]) #Imprime a segunda posição da string "a"
print("\n")

print(b[0]) #Imprime a primeira posição da string "b"
print(b[1]) #Imprime a segunda posição da string "b"
print(b[2]) #Imprime a terceira posição da string "b"
print(b[3]) #Imprime a quarta posição da string "b"
print(b[4]) #Imprime a quinta posição da string "b"
print("\n")

# *************************** FUNÇÔES STRINGS - IMPRESSÃO PELO ÍNDICE **************************
print(concatenar[0:6]) #Imprime do caractér 0 até o 6
print("\n")

print(concatenar[1:4]) #Imprime do caractér 1 até o 4
print("\n")
