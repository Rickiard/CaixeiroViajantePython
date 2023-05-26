import random

file = open("cidades.txt", "w")
coordenadas_escritas = set()

while len(coordenadas_escritas) < 50:
    x = random.randint(-256, 256)
    y = random.randint(-256, 256)
    coordenada = str(x) + ", " + str(y)
    
    if coordenada not in coordenadas_escritas:
        coordenadas_escritas.add(coordenada)
        file.write(coordenada + "\n")

file.close()
