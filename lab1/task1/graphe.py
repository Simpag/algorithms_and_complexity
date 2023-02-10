import sys
from time import process_time
import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(100_000_000)

def get_buffer(i, buffer):
    if i < 0:
        return 10**10
    
    return buffer[i]
    
def bottom_up(n):
    if n < 0:
        return 10**10
    elif n == 0:
        return 0

    buffer = [0 for i in range(n+1)]
    for i in range(1,n+1):
        buffer[i] = min(i, 1 + get_buffer(i-a, buffer), 1 + get_buffer(i-b, buffer), 1 + get_buffer(i-c, buffer))

    return buffer[n]

def time_e(n):
    start = process_time()
    bottom_up(n)
    end = process_time()

    print(f'Time: {end-start}, {n}')
    
    return end - start


n = 2_300_000
a = 5
b = 6
c = 7
linear = [n+x for x in range(0,20)]
exponential = [2**x * n for x in range(7)]

print(linear, exponential)

linear_res = [time_e(x) for x in linear]
plt.title("Runtime")
plt.plot(linear, linear_res)
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.savefig('e_linear.png')


exponential_res = [time_e(x) for x in exponential]
plt.plot(exponential, exponential_res)
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.savefig('e_exponential.png')