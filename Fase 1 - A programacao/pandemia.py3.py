"""
    Resolução da proposta "Pandemia"

Exemplos:
A)
4 3
2 1
2 1 2
3 3 1 2
2 2 1

Deve retornar 3
B)
10 5
2 1
6 7 5 1 9 6 2
3 9 4 6
3 2 9 5
3 8 5 7
2 8 9

Deve retornar 8
C)
5 6
3 4
2 1 3
4 1 2 3 5
2 1 3
2 1 3
2 4 5
2 2 4

Deve retornar 2
"""


class Reuniao:
    def __init__(self, integrantes):
        self.integrantes = integrantes

    def get_dia(self):
        return self.dia

    def get_interantes(self):
        return self.integrantes.copy()

    def infectar(self, lista_integrantes):
        for integrante in self.integrantes:
            lista_integrantes[integrante].set_doente(True)

    def verificar_infectado(self, lista_integrantes):
        for integrante in self.integrantes:
            if lista_integrantes[integrante].get_doente():
                self.infectar(lista_integrantes)


class Amigo:
    def __init__(self, infectado=False):
        self.doente = infectado

    def get_doente(self):
        return self.doente

    def set_doente(self, infectado):
        self.doente = infectado


def main():
    numero_amigos, numero_reunioes = (int(res) for res in input().split())

    # Cria as instancias de todos os amigos
    lista_amigos = {}
    for amigoID in range(1, numero_amigos + 1):
        lista_amigos.setdefault(amigoID, Amigo())

    # Define a primeira intancia de Amigo infectada
    infectado_1a, dia_infectado = (int(res) for res in input().split())
    lista_amigos[infectado_1a].set_doente(True)

    # Cira as intancias de todas as reunioes
    lista_reunioes = {}
    for dia in range(1, numero_reunioes + 1):
        integrantes = [int(amigo) for amigo in input().split()[1:]]
        lista_reunioes.setdefault(dia, Reuniao(integrantes))

    # Infecta as outras instancias de Amigo de acordo com as reunioes
    for dia in range(dia_infectado, numero_reunioes):
        lista_reunioes[dia].verificar_infectado(lista_amigos)

    # Conta o numero final de infectados
    numero_infectados = 0
    for amigo in lista_amigos.values():
        if amigo.get_doente():
            numero_infectados += 1

    print(numero_infectados)


if __name__ == "__main__":
    main()
