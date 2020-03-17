print("Olá Mundo\n")

# ****************************************** VARIÁVEIS ******************************************
print("**** VARIÁVEIS ****")
var1 = 1 # Variável Inteira.
var2 = 1.1 # Variável Float.
var3 = "String" # Variável String.
var4 = True # Variável Booleana.

print(var1, "- Variável Inteira")
print(var2, "- Variável Float")
print(var3, "- Variável String")
print(var4, "- Variável Booleana\n")
print("\n")

# *********************************** ESTRUTURAS CONDICIONAIS ***********************************
print("**** ESTRUTURAS CONDICIONAIS ****")
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
print("\n")

# ********************************* ESTRUTURAS DE REPETIÇÃO: FOR *********************************
print("**** ESTRUTURAS DE REPETIÇÃO: FOR ****")
lista1 = [1, 3, 5, 7, 9]
lista2 = ["olá", "mundo", "!"]
lista3 = [1, "prato", "de", "trigo", "para", 1, "tigre", "triste", 0.0]

print("Lista 1:", lista1)
print("Lista 1 - FOR:")
for i in lista1:
    print(i)
print("\n")

print("Lista 2:", lista2)
print("Lista 2: - FOR")
for i in lista2:
    print(i)
print("\n")

print("Lista 3:", lista3)
print("Lista 3: - FOR")
for i in lista3:
    print(i)
print("\n")

# ******************************** ESTRUTURAS DE REPETIÇÃO: WHILE ********************************
print("**** ESTRUTURAS DE REPETIÇÃO: WHILE ****")
z = 1

print("While de 0 a 9")
while z < 10:
    print(z)
    z += 1
print("\n")

# ***************************** ESTRUTURAS DE REPETIÇÃO: FOR E RANGE *****************************
print("**** ESTRUTURAS DE REPETIÇÃO: FOR E RANGE ****")
print("For de 0 a 9:")
for i in range(10): # Imprime uma lista com 10 elementos de 0 até 9.
    print(i) 
print("\n")

print("For de 10 a 19:")
for i in range(10, 20): # Imprime uma lista de 10 elementos de 10 até 19.
    print(i) 
print("\n")

print("For de 10 a 19 de 2 em 2:")
for i in range(10, 20, 2): # Imprime uma lista de 10 elementos de 10 até 19 de 2 em 2.
    print(i) 
print("\n")

# ******************************************** INPUT ********************************************
print("**** INPUT ****")
numero = input("Digite um número: ") # Input de números.
print("O número digitado é:", numero)
print("\n")

nome = input("Digite um nome: ") # Input de string.
print("Bem-vindo(a)", nome)
print("\n")

# ******************************** FUNÇÔES STRINGS - CONCATENAÇÃO ********************************
print("**** FUNÇÔES STRINGS - CONCATENAÇÃO ****")
a = "Oh"
b = "Sehun"

concatenar = a + " " + b # Junção de strings.
print("Concatenação:", concatenar)

tamanho = len(concatenar)
print("Tamanho da concatenação:", tamanho)
print("\n")

# **************************** FUNÇÔES STRINGS - NAVEGAÇÂO PELO ÍNDICE **************************
print("**** FUNÇÔES STRINGS - NAVEGAÇÂO PELO ÍNDICE ****")
print(a[0]) # Imprime a primeira posição da string "a".
print(a[1]) # Imprime a segunda posição da string "a".
print("\n")

print(b[0]) # Imprime a primeira posição da string "b".
print(b[1]) # Imprime a segunda posição da string "b".
print(b[2]) # Imprime a terceira posição da string "b".
print(b[3]) # Imprime a quarta posição da string "b".
print(b[4]) # Imprime a quinta posição da string "b".
print("\n")

# **************************** FUNÇÔES STRINGS - IMPRESSÃO PELO ÍNDICE **************************
print("**** FUNÇÔES STRINGS - IMPRESSÃO PELO ÍNDICE ****")
print("String:", concatenar)
print("Caracteres de 0 a 6 da String", concatenar[0:6]) # Imprime do caractér 0 até o 6.
print("\n")

print("String:", concatenar)
print("Caracteres de 1 a 4 da String",concatenar[1:4]) # Imprime do caractér 1 até o 4.
print("\n")

# ********************************** FUNÇÔES STRINGS - MINÚSCULO ********************************
print("**** FUNÇÔES STRINGS - MINÚSCULO ****")
# variável.lower() : Função que deixa todos os caracteres minúsculos.

print("String normal:", concatenar)
print("String minúscula:", concatenar.lower())
print("\n")

# variável = variável.lower() : Adota a string toda minúscula.

# ********************************** FUNÇÔES STRINGS - MAIÚSCULO ********************************
print("**** FUNÇÔES STRINGS - MAIÚSCULO ****")
# variável.upper() : Função que deixa todos os caracteres maiúsculos.

print("String normal:", concatenar)
print("String minúscula:", concatenar.upper())
print("\n")

# variável = variável.upper() : Adota a string toda maiúscula.

# ************************************ FUNÇÔES STRINGS - STRIP **********************************
print("**** FUNÇÔES STRINGS - STRIP ****")
# Remove espaços ou caracteres especiais ao final da string.

print(concatenar.strip())
print("\n")

# ************************************ FUNÇÔES STRINGS - SPLIT **********************************
print("**** FUNÇÔES STRINGS - SPLIT ****")
# Converte uma string em uma lista (CASE SENSITIVE)

minha_string = "CORONA VAIRUS CORONA VARIUS GETTING REAL GETTING REAL"
print("String:", minha_string)

minha_string = minha_string.split("C")
print("String com split pulando o C:", minha_string)
print("\n")

# **************************** FUNÇÔES STRINGS - BUSCA DE SUBSTRINGS ****************************
print("**** FUNÇÔES STRINGS - BUSCA DE SUBSTRINGS ****")
# Busca um pedaço exato dentro de uma string e retorna o índice desse pedaço.

outra_string = "O rato roeu a roupa do rei de Roma"
print("String:", outra_string)
print("\n")

busca = outra_string.find("rei")
print("Indíce no qual 'rei' começa a aparecer:", busca)
print("\n")

print("Imprimindo a partir de 'rei':", outra_string[busca:])
print("\n")

# ********************************** FUNÇÔES STRINGS - REPLACE **********************************
print("**** FUNÇÔES STRINGS - REPLACE ****")
# Substitui partes de uma String.

outra_string = outra_string.replace("rei", "rainha")
print("Substituindo rei por rainha:", outra_string)
