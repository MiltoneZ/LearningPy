# Esto es una lista[Array]
lista = [5, 6, 3, 2, 9]
it = iter(lista)

for i in lista:
    print("-", next(it))
print(lista)

# for to print the list
for i in range(5, 20, 2):
    print(i, end=" ")

# Ciclo for en forma descendant
for i in range(5, 0, -1):
    print(i, end=" ")

print("\n")

# Un For con un rango de 6 characters a imprimir
for i in range(6):
    print(i, end=" ")

print("\n")
