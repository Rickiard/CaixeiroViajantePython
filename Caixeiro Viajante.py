import math
import sys
import os
import platform

cidades = []

def distance (location1, location2):

    x, y = location1
    a, b = location2

    return math.sqrt(pow(x - a, 2) + pow(y - b, 2))

def CaixeiroViajante(cidades):
    melhorRota = [cidades[0]]
    menorDistancia = 0
    jaPassou = set([cidades[0]])

    while len(melhorRota) != len(cidades):
        cidade_atual = melhorRota[-1]
        distancia_minima = float('inf')
        proxima_cidade = None

        for cidade in cidades:
            if cidade not in jaPassou:
                distancia = distance(cidade_atual, cidade)
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    proxima_cidade = cidade

        if proxima_cidade is None:
            break

        melhorRota.append(proxima_cidade)
        jaPassou.add(proxima_cidade)
        menorDistancia += distancia_minima

    melhorRota.append(cidades[0])

    menorDistancia += distance(melhorRota[-1], melhorRota[0])

    return (melhorRota, menorDistancia)

def ler_cidades_do_ficheiro(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            for linha in ficheiro:
                x, y = map(float, linha.split(','))
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
    N = 0
    while N <= 1:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        N = int(input("Digite o número de cidades: "))
        if  N <= 1:
            print("\nNão pode ter essa quantidade\n")
            input()
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
    elif op == 2: 
        ler_cidades_teclado()
        printar(cidades)
    elif op == 3: sys.exit()
    else: 
        print("Opção inexistente! Tente novamente...")
        input()
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        menu()

while True:
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    cidades.clear()
    menu()
