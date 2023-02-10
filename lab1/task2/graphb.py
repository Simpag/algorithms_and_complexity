import sys
from time import process_time
import numpy as np
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


n = 4_200_000 #2700
linear = [n+x for x in range(0,50)]
exponential = [2**x * n for x in range(3)] # over 3 gives killed, number is 33 600 000

print(linear, exponential)

linear_res = [time_b(x) for x in linear]
plt.title("Runtime")
plt.plot(linear, linear_res)
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.savefig('b_linear_short.png')


exponential_res = [time_b(x) for x in exponential]
plt.title("Runtime")
plt.plot(exponential, exponential_res)
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.savefig('b_exponential.png')

linear = [n+x for x in range(0,1000)]
linear_res = [time_b(x) for x in linear]
plt.title("Runtime")
plt.plot(linear, linear_res)
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.savefig('b_linear.png')