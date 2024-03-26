# Teoria basic de Python.
# Aqui podremos ver como se identified las funciones mas basics,
# Pero son las mas utilization en Python.

# Esto es una lista[Array]
# Cualquier arreglo puede ser iterada, esto busca sus valores por segmento
# Puede incluso verse en palabras.
lista = [5, 6, 3, 2, 9]
it = iter(lista)

for i in lista:
    print("-", next(it))
print(lista)

# Las cosas que no son iterables son los numeros enteros (19, 10...)

# El siguiente print es para dar un salto de linea
# print("\n")

# for to print the list
for i in range(5, 20, 2):
    print(i, end=" ")

print("\n")

# Ciclo for en forma descendant
for i in range(5, 0, -1):
    print(i, end=" ")

print("\n")

# Un For con un rango de 6 characters a imprimir
for i in range(6):
    print(i, end=" ")

print("\n")

# Un ciclo while para imprimir los numeros de 0 al 10
# Mientras se cumpla la condicion que seleccionemos

x = 0
while x < 10:
    x += 1
    print(x, end=" ")

print("\n")

# u
i = 0
j = 0
while i < 3:
    while j < 3:
        print(F"{i}-{j}", end=" ")
        j += 1
    i += 1
    j = 0

print("\n")

# Fibonacci en python
a, b = 0, 1
while b < 25:
    print(b, end=" ")
    a, b = b, a + b

print("\n")

# Arbol de navidad en python
z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1