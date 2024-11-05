import time
def fibonacci_search(arr, x):
    n = len(arr)

    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m2 + fib_m1

    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)

        if arr[i] < x:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        elif arr[i] > x:
            fib_m = fib_m2
            fib_m1 -= fib_m2
            fib_m2 = fib_m - fib_m1

        else:
            return i

    if fib_m1 and arr[offset + 1] == x:
        return offset + 1

    return -1

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

#for i in range(0,10000):
   # arr.append(i)
x = 21
inicio = time.time()
resultado = fibonacci_search(arr, x)
fim = time.time()
print("Elemento encontrado no índice:", resultado)
print(fim - inicio)
