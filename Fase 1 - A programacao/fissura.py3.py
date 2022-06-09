def main(numero_linhas, forca_erupcao):
    """
    Retorna a matriz com o rastro de invasao da lava
    """

    lista_linhas = [n for n in range(numero_linhas)]
    matriz = [[] for n in lista_linhas]

    # Simulador
    for numero_contagem in lista_linhas:
        linha = input()
        for altura in linha:
            matriz[numero_contagem] += [int(altura)]

    if matriz[0][0] <= forca_erupcao:
        areas_afetadas = [(0, 0)]

        while len(areas_afetadas) != 0:
            area_atual = areas_afetadas[0]
            areas_afetadas.pop(0)
            matriz[area_atual[0]][area_atual[1]] = 10

            esquerda = area_atual[1] + 1
            direita = area_atual[1] - 1
            baixo = area_atual[0] + 1
            cima = area_atual[0] - 1

            if direita in lista_linhas:
                quadrante_direita = matriz[area_atual[0]][area_atual[1] - 1]
                if quadrante_direita <= forca_erupcao:
                    areas_afetadas += [(area_atual[0], direita)]

            if baixo in lista_linhas:
                quadrante_baixo = matriz[area_atual[0] + 1][area_atual[1]]
                if quadrante_baixo <= forca_erupcao:
                    areas_afetadas += [(baixo, area_atual[1])]

            if esquerda in lista_linhas:
                quadrante_esquerda = matriz[area_atual[0]][area_atual[1] + 1]
                if quadrante_esquerda <= forca_erupcao:
                    areas_afetadas += [(area_atual[0], esquerda)]

            if cima in lista_linhas:
                quadrante_cima = matriz[area_atual[0] - 1][area_atual[1]]
                if quadrante_cima <= forca_erupcao:
                    areas_afetadas += [(cima, area_atual[1])]

    # Visualizador
    for linha in matriz:
        string = ""
        for numero in linha:
            if numero == 10:
                string += "*"
            else:
                string += str(numero)
        print(string)


parametros = [int(param) for param in input().split()]
main(parametros[0], parametros[1])
