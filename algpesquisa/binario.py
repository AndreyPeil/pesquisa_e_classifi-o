#binario recursivo
import time
def binary_search_re(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_re(arr, low, mid - 1, x)
        else:
            return binary_search_re(arr, mid + 1, high, x)
    else:
        return -1

arr = []
for i in range(0,10000):
    arr.append(i)

x = 10
inicio = time.time()
result = binary_search_re(arr, 0, len(arr)-1, x)
fim = time.time()
print("Element is present at index", str(result))
print(fim - inicio)


#binario iterativo
import time

def binary_search_in(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


arr = []
for i in range(0,10000):
    arr.append(i)
x = 10

inicio = time.time()
result = binary_search_in(arr, x)
fim = time.time()
print("Element is present at index", str(result))
print(fim - inicio)
