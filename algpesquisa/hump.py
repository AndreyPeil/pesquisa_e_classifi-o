#jump search
import time
import math

def jumpSearch( arr , x , n ):

    step = math.sqrt(n)

    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev

    return -1

arr = []
for i in range(0,10000):
    arr.append(i)
x = 55
n = len(arr)
start = time.time()
index = jumpSearch(arr, x, n)
end = time.time()

print("Number" , x, "is at index" ,"%.0f"%index)
print(end - start)
