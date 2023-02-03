import sys
from time import process_time
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(100_000_000)

def f(x,y,p,k,buffer):
    if y == 0:
        return 1
    elif x == 0 and y > 0:
        return 0
    elif buffer[x][y] is not None:
        return buffer[x][y]

    buffer[x][y] = p*f(x-1, y-1, p,k, buffer) + (1-p) * f(x-1, k, p,k, buffer)
    return buffer[x][y]

def time_a(x):
    k = x//2
    buffer = [[None for j in range(k+1)] for i in range(x+1)]
    p = 0.99
    start = process_time()
    f(x,k,p,k,buffer)
    end = process_time()
    
    return end - start


for i in range(1_000,10_000, 100):
    print(time_a(i), i)