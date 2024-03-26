# Teoria basic de Python.
# Aqui podremos ver como se identified las funciones mas basics,
# Pero son las mas utilization en Python.

# Esto es una lista[Array]
lista = [5, 6, 3, 2, 9]
it = iter(lista)

for i in lista:
    print("-", next(it))
print(lista)

print("\n")

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
