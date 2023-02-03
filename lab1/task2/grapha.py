import sys
from time import process_time
import numpy as np
import matplotlib.pyplot as plt

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

    print(f'Time: {end-start}, {x}')
    
    return end - start


n = 2700
linear = [n+x for x in range(0,1001)]
exponential = [2**x * n for x in range(3)] # over 3 gives seg fault, number is 21600

print(linear, exponential)

linear_res = [time_a(x) for x in linear]
plt.title("Runtime")
plt.plot(linear, linear_res)
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.savefig('a_linear.png')


exponential_res = [time_a(x) for x in exponential]
plt.plot(exponential, exponential_res)
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.savefig('a_exponential.png')