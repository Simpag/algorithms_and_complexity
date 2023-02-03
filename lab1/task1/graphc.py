import sys
from time import process_time
import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(100_000_000)

def memoization(n):
    b_buffer = [None for x in range(n+1)]

    return memoization_helper(n, b_buffer)
    
def memoization_helper(n, buffer):    
    if n < 0:
        return 10**10
    elif n == 0:
        return 0
    elif buffer[n] is not None:
        return buffer[n]
    else:
        buffer[n] = min(n, 1 + memoization_helper(n-a, buffer), 1 + memoization_helper(n-b, buffer), 1 + memoization_helper(n-c, buffer))

    return buffer[n]

def time_b(n):
    start = process_time()
    memoization(n)
    end = process_time()

    print(f'Time: {end-start}, {n}')
    
    return end - start


n = 82
a = 5
b = 6
c = 7
linear = [n+x for x in range(0,20)]
exponential = [2**x * n for x in range(3)] # over 3 gives seg fault, number is 21600

print(linear, exponential)

linear_res = [time_b(x) for x in linear]
plt.title("Runtime")
plt.plot(linear, linear_res)
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.savefig('c_linear.png')


exponential_res = [time_b(x) for x in exponential]
plt.plot(exponential, exponential_res)
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.savefig('c_exponential.png')