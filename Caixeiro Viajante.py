import math

cidades = [(0, 0), (1, 0), (3, 0), (10, 0), (2, 0)]

N = len(cidades) - 1

def distance (location1, location2):

    x, y = location1
    a, b = location2

    return math.sqrt(pow(x - a, 2) + pow(y - b, 2))

def CaixeiroViajante (cidades):
    melhorRota = [(0, 0)]
    menorDistancia = 10000000000
    a = 1000000
    o = 0
    pos = 1
    jaPassou = []

    while len(melhorRota) != len(cidades):
        aux = 10000000
        ant = 100000000
        dist = 1000000000
        for i in range(len(cidades)):
            if i != o and i not in jaPassou:
                a = distance(cidades[o], cidades[i])
                if aux > a:
                    if pos in range(len(melhorRota)) and cidades[i] not in melhorRota:
                        del (melhorRota[-1])
                        melhorRota.append(cidades[i])
                        aux = a
                    elif cidades[i] not in melhorRota:
                        melhorRota.append(cidades[i])
                        aux = a
                    if i == len(cidades):
                        jaPassou.append(o)
                        o = i

                if ant > a and a != 0:
                    menorDistancia = a

                ant = menorDistancia

        pos = pos + 1

    # for o in range(1, len(cidades)):
      #  for i in range(len(cidades)):
       #     if distance(cidades[a], cidades[i]) < dist and i != a:
        #        dist = distance(cidades[a], cidades[i])

         #       if dist < menorDistancia:
          #          melhorRota.append(cidades[i])
                
           #     if dist < menorDistancia:
            #        a = i
        
       # if menorDistancia > dist:
        #    menorDistancia = dist
    
    return (melhorRota, menorDistancia)

melhorRota, menorDistancia = CaixeiroViajante(cidades)
print("\nMelhor rota:", melhorRota)
print("\nMenor distância:", menorDistancia, "\n")

