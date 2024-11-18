class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChained:
    def __init__(self, size):
        self.size = size
        self.table = {i: None for i in range(size)}

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None 

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return False 
    def display(self):
        for index, node in self.table.items():
            print(f"Índice {index}:", end=" ")
            current = node
            while current:
                print(f"({current.key}, {current.value}) ->", end=" ")
                current = current.next
            print("None")

htable = HashTableChained(5)

htable.insert("chave1", "valor1")
htable.insert("chave2", "valor2")
htable.insert("chave3", "valor3")
htable.insert("chave1", "valor atualizado")  

htable.display()

print(htable.search("chave1"))  
print(htable.search("chaveX"))  

htable.delete("chave1")
htable.display()
