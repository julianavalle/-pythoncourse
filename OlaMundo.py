print("Olá Mundo\n")

# ***************************************** VARIÁVEIS *****************************************
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

# ******************************* ESTRUTURAS DE REPETIÇÃO: FOR *******************************
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
    