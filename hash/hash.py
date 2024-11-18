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
            while current.next:
                if current.key == key: 
                    current.value = value
                    return
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


htable = HashTableChained(10)
htable.insert("chave1", 1000)
htable.insert("chave2", "valor2")
print(htable.search("chave2"))  
print(htable.search("chave1"))  

