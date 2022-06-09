"""
    Promoção Primeira
"""

import functools as ft


def soma(val1, val2): return val1 + val2


def verificar_matriz(matriz, ignorar, valores=[0, 1]):
    for termo, termo_id in zip(matriz, range(len(matriz))):
        if termo in valores and not termo_id in ignorar:
            return termo_id, termo
        else:
            pass

    return -1, -1


num_cidades = int(input(""))

cidades = [[-1 for num2 in range(num_cidades)] for num in range(num_cidades)]

for num in range(num_cidades - 1):
    entrada = [int(val) for val in input().split()]
    entrada[0] -= 1
    entrada[1] -= 1

    cidades[entrada[0]][entrada[1]] = entrada[2]
    cidades[entrada[1]][entrada[0]] = entrada[2]


cidades_verificadas = []
rotas = []
rotas_ = []

for cidade, cidade_id in zip(cidades, range(num_cidades)):
    cidades_verificadas = [cidade_id]

    rota = str(cidade_id) + " "
    rota_ = ""

    matriz_rotas = cidade
    while len(cidades_verificadas) != num_cidades:
        val, passagem = verificar_matriz(matriz_rotas, cidades_verificadas)

        if val == -1:
            rota = ft.reduce(lambda n1, n2: "{} {} ".format(
                n1, n2), rota.split()[:-1])
            if rota[-1] != " ":
                rota += " "
            rota_ = rota_[:-1]
        else:
            rota += str(val) + " "
            rota_ += str(passagem)

        if len(rota.split()) > 1 and not rota in rotas:
            rotas += [rota]
            rotas_ += [rota_]

        if val != -1:
            cidades_verificadas += [val]
            matriz_rotas = cidades[val]
        else:
            indicie = int(rota.split()[-1])
            matriz_rotas = cidades[indicie]

maior = ""
tamanho_maior = len(maior)
for percurso, percurso_id in zip(rotas_, range(len(rotas_))):
    tamanho = len(percurso)

    lista_ideal1 = ft.reduce(soma, [str(num % 2) for num in range(tamanho)])
    lista_ideal2 = ft.reduce(soma, [str((num + 1) % 2)
                             for num in range(tamanho)])

    if percurso == lista_ideal1 or percurso == lista_ideal2:
        if tamanho >= tamanho_maior:
            maior = percurso
            tamanho_maior = tamanho

print(len(maior) + 1)
