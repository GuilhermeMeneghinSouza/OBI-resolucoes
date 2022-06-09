def main(distancia):
    """
    Retorna o numero do sensor que a particula atingiu
    """
    numero = (distancia - 5) % 8

    if numero in [1, 2, 3]:
        return numero
    else:
        return None


if __name__ == '__main__':
    print(main(int(input())))
