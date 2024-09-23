import random
import os
import heapq

def create_document():
    with open("externo.txt", "w") as file:
        for i in range(1000):
            file.write(str(random.randint(0, 1000)) + "\n")

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

def merge_sort_external(externo, memoria):
    block_size = memoria // 4  
    block_files = []

    with open(externo, "r") as file:
        while True:
            numeros = []
            for _ in range(block_size):
                line = file.readline()
                if not line:
                    break
                numeros.append(int(line.strip()))
            
            if not numeros:
                break
            
            sorted_numeros = merge_sort(numeros)
            
            block_file = f"block_{len(block_files)}.txt"
            with open(block_file, "w") as bf:
                for num in sorted_numeros:
                    bf.write(str(num) + "\n")
            block_files.append(block_file)

    merge_sorted_files(block_files, "output_sorted.txt")

    for block_file in block_files:
        os.remove(block_file)

def merge_sorted_files(block_files, output_file):
    min_heap = []
    
    file_iters = {file: open(file, "r") for file in block_files}
    
    for file, f in file_iters.items():
        num = f.readline().strip()
        if num:
            heapq.heappush(min_heap, (int(num), file))
    
    with open(output_file, "w") as outfile:
        while min_heap:
            smallest, smallest_file = heapq.heappop(min_heap)
            outfile.write(str(smallest) + "\n")
            
            next_num = file_iters[smallest_file].readline().strip()
            if next_num:
                heapq.heappush(min_heap, (int(next_num), smallest_file))
    
    for f in file_iters.values():
        f.close()

create_document()
memoria = 1024 
merge_sort_external("externo.txt", memoria)
