import math
import sys
import os
import platform

cidades = [(0, 0), (1, 0), (3, 0), (10, 0), (2, 0)]

def menu():
    op = int(input("\nCaixeiro Viajante:\n\n 1: Ler através de ficheiro\n 2: Ler através de teclado\n 3: Sair do programa\n\n"))
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    if op == 1: 
        print("1") 
        menu()
    elif op == 2: 
        print("2")
        
        menu()
    elif op == 3: sys.exit()
    else: 
        print("Opção inexistente! Tente novamente...")
        input()
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        menu()

menu()

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
    
    return (melhorRota, menorDistancia)

melhorRota, menorDistancia = CaixeiroViajante(cidades)
print("\nMelhor rota:", melhorRota)
print("\nMenor distância:", menorDistancia, "\n")

input()

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

menu()
