#cria a classe node com atributos next e data
class Node:
    def __init__(self, data=None) -> None:
        self.data = data 
        self.next = None

#Cria a classe linkedlist
class LinkedList:

    #primero node
    def __init__(self) -> None:
        self.head = None
    
    #Método append de nodos
    def append(self, data):
        #cria novo nodo
        new_node = Node(data)  
        #Se o primero nodo for null, da o primeiro valor como head
        if self.head is None:
            self.head = new_node
        else:
            #Current node = primeiro
            current = self.head
            #Se tiver mais que um nodo
            while current.next:
                current = current.next 
            #proximo nodo é o novo nodo
            current.next = new_node
        
    def print_list(self):
        #pritna a lista
        if self.head is None:
            print("Lista vazia")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

import random

# funcaoes feitas no outro exercicio
def ordenados():
    data = [1, 2, 3, 4, 6, 5]
    for j in range(1, len(data)): 
        temp = data[j]
        i = j - 1
        while i >= 0 and temp < data[i]:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = temp
    return data
        
def ordenados_inversa():
    data = [1, 2, 3, 4, 5]
    lista_rev = data[::-1]
    return lista_rev
    
def elemetno_dup():
    data = [1, 2, 1, 3, 4, 5]
    for j in range(1, len(data)): 
        temp = data[j]
        i = j - 1
        while i >= 0 and temp < data[i]:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = temp
    return data
        
def random_aa():
    lista = []
    for i in range(0, 6):
        a = random.randint(0, 6)
        if a in lista:
            lista.remove(a)
        else:
            lista.append(a)
    for j in range(1, len(lista)): 
        temp = lista[j]
        i = j - 1
        while i >= 0 and temp < lista[i]:
            lista[i + 1] = lista[i]
            i = i - 1
        lista[i + 1] = temp
    return lista

linked_list = LinkedList()
linked_list.append(ordenados())
linked_list.append(ordenados_inversa())
linked_list.append(elemetno_dup())
linked_list.append(random_aa())

linked_list.print_list()
