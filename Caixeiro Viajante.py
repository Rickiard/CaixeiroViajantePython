import math

cidades = [(0, 0), (1, 2), (3, 1), (2, 4), (4, 3)]

N = len(cidades) - 1

def distance (location1, location2):

    x, y = location1
    a, b = location2

    return math.sqrt(pow(x - a, 2) + pow(y - b, 2))

def CaixeiroViajante (cidades):
    melhorRota = [(0, 0)]
    menorDistancia = 10000000000
    a = 0
    dist = 1000000000

    for o in range(1, len(cidades)):
        for i in range(len(cidades)):
            if distance(cidades[a], cidades[i]) < dist and i != a:
                dist = distance(cidades[a], cidades[i])

                if dist < menorDistancia:
                    melhorRota.append(cidades[i])
                
                if dist < menorDistancia:
                    a = i
        
        if menorDistancia > dist:
            menorDistancia = dist
    
    return (melhorRota, menorDistancia)

