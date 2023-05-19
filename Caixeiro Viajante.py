import math
import sys
import os
import platform

cidades = []

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

def distance (location1, location2):

    x, y = location1
    a, b = location2

    return math.sqrt(pow(x - a, 2) + pow(y - b, 2))

def CaixeiroViajante (cidades):
    melhorRota = [cidades[0]]
    menorDistancia = 0
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

        pos = pos + 1
    melhorRota.append(cidades[0])
    for i in range(len(melhorRota) - 1):
        menorDistancia = menorDistancia + distance(melhorRota[i], melhorRota[i+1])
    return (melhorRota, menorDistancia)

def ler_cidades_do_ficheiro(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            for linha in ficheiro:
                x, y = map(int, linha.split(','))
                cidades.append((x, y))      
            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
            print("Lista carregada:", cidades)
            input()
    except FileNotFoundError:
        print("\nErro: Arquivo não encontrado. Tente novamente... ")
        input()
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        ler_cidades_do_ficheiro(nome_ficheiro = input("Introduza o nome do ficheiro: "))

def ler_cidades_teclado():
    N = int(input("Digite o número de cidades: "))
    for i in range(N):
        cidade = eval(input(f"\nQuais são as coordenadas da cidade {i+1} ('x,y'): "))
        cidades.append(cidade)
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print("Lista carregada:", cidades)
    input()

def printar(cidades):
    melhorRota, menorDistancia = CaixeiroViajante(cidades)
    print("Melhor rota:", melhorRota)
    print("\nMenor distância:", menorDistancia, "\n")
    input()

def menu():
    op = int(input("Caixeiro Viajante:\n\n 1: Ler através de ficheiro\n 2: Ler através de teclado\n 3: Sair do programa\n\n"))
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    if op == 1:
        ler_cidades_do_ficheiro(nome_ficheiro = input("Introduza o nome do ficheiro: "))
        printar(cidades)
... (21 linhas)
