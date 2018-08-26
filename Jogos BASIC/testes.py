numero = []
tamanho = int(input("Tamanho: "))

for n in range(1,tamanho+1):
    n = int(input("Dgt as letras: "))
    numero.append(n)

numero = [n * n for n in numero]


print(numero)


#________________________________________________________________________________

inteiros = [1,2,3,4,5]
pares = [n for n in inteiros if n % 2 == 0]
print(pares)

