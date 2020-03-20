print("Sem List Comprehension")
x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)
print("\n")

print("Com List Comprehension")
#a = [1, 2, 3, 4, 5]
#b = [valor_a_adicionar laço condição]

a = [1, 2, 3, 4, 5]
b = [i**2 for i in x]
c = [i for i in x if i%2 == 1]
d = [i**2 for i in x if i%2 == 0]
print(a)
print(b)
print(c)
print(d)
print("\n")