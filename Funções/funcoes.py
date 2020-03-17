def soma(x, y):
    return (x + y)

def mult(x, y):
    return (x * y)

a = 2
b = 3

s = soma(a, b)
print(a, "+", b, "=", s)

m = mult(a, b)
print(a, "*", b, "=", m)

print(m, "+", s, "=", soma(s, m))

