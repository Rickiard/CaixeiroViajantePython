import math

cidades = [(0, 0), (1, 2), (3, 1), (2, 4), (4, 3)]

N = len(cidades) - 1

def distance (location1, location2):

    x, y = location1
    a, b = location2

    return math.sqrt(pow(x - a, 2) + pow(y - b, 2))

def CaixeiroViajante (cidades):
    melhorRota = []
    menorDistancia = 0

    for i in range(len(cidades)):
        dict = {CaixeiroViajante(cidades):cidades[i]}

    return (melhorRota, menorDistancia)

melhorRota, menorDistancia = CaixeiroViajante(cidades)
print("Melhor rota:", melhorRota)
print("Menor distância:", menorDistancia)