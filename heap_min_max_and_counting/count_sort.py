def conting(array):
    if not array:
        return array
    

    val_min = min(array)
    val_max = max(array)

    range_elemento = val_max - val_min + 1
    cont = [0] * (range_elemento)

    for num in array:
        cont[num  - val_min] += 1
    
    index = 0
    for i in range(range_elemento):
        while cont[i] > 0:
            array[index] = i
            index += 1
            cont[i] -= 1
    return array

array = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = conting(array)
print("Array ordenado é", sorted_arr)
