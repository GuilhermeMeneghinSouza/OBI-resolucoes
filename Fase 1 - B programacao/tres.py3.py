import functools as ft


numeroChocolates = int(input())

listaPrecos = [int(input()) for x in range(numeroChocolates)]
print("="*10)

listaPrecos.sort(reverse=True)

numtrios = (numeroChocolates - numeroChocolates % 3) / 3

promocao = []
contador = 0
while contador/3 != numtrios:
    promocao += [listaPrecos[contador: contador + 3]]
    contador += 3

pagar = listaPrecos[contador:]

for trio in promocao:
    pagar += trio[:2]

total = ft.reduce(lambda x, y: x + y, pagar)

print(total)
