import random

def bubble(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def menu():
    while True:
        print("1 - Ordenada")
        print("2 - Com números repetidos")
        print("3 - Inversa")
        print("4 - Aleatória")
        opc = int(input("Qual a sua opção: "))
        if 1 <= opc <= 4:
            return opc
        else:
            print("Opção inválida! Tente novamente.")

def main():
    
        opc = menu()
        if opc == 1:
            lista = [1, 2, 3, 4, 5, 6]
        elif opc == 2:
            lista = [1, 2, 1, 3, 4, 4, 5, 5, 3, 6, 6]
        elif opc == 3:
            lista = [6, 5, 4, 3, 2, 1]
        elif opc == 4:
            lista = [random.randint(0, 9) for x in range(6)]

        print("Lista antes da ordenação:", lista)
        bubble(lista)
        print("Lista após a ordenação:", lista)

main()
