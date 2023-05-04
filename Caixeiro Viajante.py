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
    a = 0
    dist = 1000000000
    for o in range(len(cidades))
        for i in range(len(cidades))
            if distance(cidades[a], cidades[i]) < dist:
                dist = distance(cidades[a], cidades[i])
                del melhorRota[-1]
                melhorRota.append(cidades[i])
                a = i

        menorDistancia = min(dists)
    
    return (melhorRota, menorDistancia)

melhorRota, menorDistancia = CaixeiroViajante(cidades)
print("Melhor rota:", melhorRota)
print("Menor distância:", menorDistancia)

