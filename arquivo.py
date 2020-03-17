arquivo = open("arquivo.txt")

linhas = arquivo.readlines() #Lê o arquivo por linhas
print(linhas) #Coloca e imprime as linhas dentro de uma lista
print("\n")

for linha in linhas:
    print(linha) #Lê as linhas separadas
print("\n")

texto_completo = arquivo.read() #Lê tudo
print(texto_completo)

w = open("arquivo2.txt", "w") #Cria o arquivo 2

w.write("Esse é o novo CORONOVAIRUS") #Escreve no arquivo 2

w.close()

z = open("arquivo.txt", "a") #Todas as vezes que executar irá gravar essa frase no arquivo
z.write("\nEsse é o novo CORONOVAIRUS") #Escreve no arquivo 2

 

