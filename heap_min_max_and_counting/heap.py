import random
import time

def heapfy(array, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and array[i] < array[esquerda]:
        maior = esquerda

    if direita < n and array[maior] < array[direita]:
        maior = direita

    if maior != i:
        array[i], array[maior] = array[maior], array[i]

        heapfy(array, n, maior)

def heap_sort_max(array):
    n = len(array)

    for i in range(n // 2 -1, -1, -1):
        heapfy(array, n, i)

    for i in range(n -1, 0, -1):
        array[i], array[0], array[i]
        heapfy(array, i, 0)

def heap_sort_min(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapfy(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0], array[i]
        heapfy(array, i, 0)


def main():
    while True:
        print("Escolha um dos modos: ")
        print("1 - Máximo")
        print("2 - Mínimo")
        escolha_modo = int(input("Escolha: "))

        if escolha_modo == 1:
            print("Escolha o que fazer: ")
            print("1 - lista desordenada")
            print("2 - lista ordenada")
            print("3 - aleatoria")
            print("4 - invertida")
            escolha = int(input("Escolha: "))
            if escolha == 1:
                tempo_i = time.time()
                lista = random.sample(range(1, 1001), 1000)
                heap_sort_max(lista)
                tempo_f = time.time()
                print(lista)
                print(tempo_f - tempo_i)
            elif escolha == 2:
                tempo_i = time.time()
                lista = [i for i in range(1, 1001)]
                heap_sort_max(lista)
                tempo_f = time.time()
                print(lista)
                print(tempo_f - tempo_i)
            elif escolha == 3:
                tempo_i = time.time()
                lista = [random.randint(1, 1000) for _ in range(1000)]
                heap_sort_max(lista)
                tempo_f = time.time()
                print(lista)
                print(tempo_f - tempo_i)
            elif escolha == 4:
                tempo_i = time.time()
                lista = [i for i in range(1000, 0, -1)]
                heap_sort_max(lista)
                tempo_f = time.time()
                print(lista)
                print(tempo_f - tempo_i)
        elif escolha_modo == 2:
            print("Escolha o que fazer: ")
            print("1 - lista desordenada")
            print("2 - lista ordenada")
            print("3 - aleatoria")
            print("4 - invertida")
            escolha = int(input("Escolha: "))
            if escolha == 1:
                tempo_i = time.time()
                lista = random.sample(range(1, 1001), 1000)
                heap_sort_min(lista)
                tempo_f = time.time()
                print(lista)
                print(tempo_f - tempo_i)
            elif escolha == 2:
                tempo_i = time.time()
                lista = [i for i in range(1, 1001)]
                heap_sort_min(lista)
                tempo_f = time.time()
                print(tempo_f - tempo_i)
                print(lista)
            elif escolha == 3:
                tempo_i = time.time()
                lista = [random.randint(1, 1000) for _ in range(1000)]
                heap_sort_min(lista)
                tempo_f = time.time()
                print(lista)
                print(tempo_f - tempo_i)
            elif escolha == 4:
                tempo_i = time.time()
                lista = [i for i in range(1000, 0, -1)]
                heap_sort_min(lista)
                tempo_f = time.time()
                print(lista)
                print(tempo_f - tempo_i)
main()
