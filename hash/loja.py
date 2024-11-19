class File:
    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.size = size

    def __repr__(self):
        return f"File(Name: {self.name}, Path: {self.path}, Size: {self.size} KB)"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = {i: [] for i in range(size)}

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, file):
        index = self._hash(file.name)
        for existing_file in self.table[index]:
            if existing_file.name == file.name:
                print(f"Erro: O arquivo '{file.name}' já existe.")
                return
        self.table[index].append(file)
        print(f"Arquivo '{file.name}' adicionado com sucesso.")

    def search(self, name):
        index = self._hash(name)
        for file in self.table[index]:
            if file.name == name:
                return file
        return None

    def remove(self, name):
        index = self._hash(name)
        for i, file in enumerate(self.table[index]):
            if file.name == name:
                del self.table[index][i]
                print(f"Arquivo '{name}' removido com sucesso.")
                return
        print(f"Erro: O arquivo '{name}' não foi encontrado.")

    def list_files(self):
        for index, files in self.table.items():
            print(f"Índice {index}: {files if files else 'Vazio'}")

if __name__ == "__main__":
    htable = HashTable(10)

    while True:
        print('\nEscolha: ')
        print('1 - Inserir arquivo')
        print('2 - Buscar arquivo')
        print('3 - Remover arquivo')
        print('4 - Listar arquivos')
        print('5 - Sair')

        choice = int(input('Escolha: '))
        if choice == 1:
            name = input('Nome do arquivo: ')
            path = input('Caminho: ')
            size = int(input('Tamanho (KB): '))
            file = File(name, path, size)
            htable.insert(file)
        elif choice == 2:
            name = input('Nome do arquivo: ')
            result = htable.search(name)
            print(result if result else "Arquivo não encontrado.")
        elif choice == 3:
            name = input('Nome do arquivo: ')
            htable.remove(name)
        elif choice == 4:
            htable.list_files()
        elif choice == 5:
            break
        else:
            print('Escolha inválida.')

    
