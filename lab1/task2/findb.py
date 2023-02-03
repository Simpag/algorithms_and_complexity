import sys
from time import process_time
import matplotlib.pyplot as plt

sys.setrecursionlimit(100_000_000)

def g(x,k,p,buffer):
    if x < k:
        return 0.0
    elif x == k:
        return p**k
    elif buffer[x] is not None:
        return buffer[x]
        
    buffer[x] = g(x-1,k,p,buffer) + p**k * (1-p) * (1 - g(x-k-1,k,p,buffer))
    return buffer[x]

def time_b(n):
    buffer = [None for x in range(n+1)]
    k = n//2
    p = 0.99

    start = process_time()
    g(n,k,p,buffer)
    end = process_time()

    print(f'Time: {end-start}, {n}')
    
    return end - start


for i in range(30_000,100_000, 1000):
    time_b(i) # gets segfault immedietly 