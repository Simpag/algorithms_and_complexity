import sys
from time import process_time
import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(100_000_000)

def recursive_a(n):
    if n < 0:
        return np.inf
    elif n == 0:
        return 0
    
    return min((n, 1 + recursive_a(n-a), 1 + recursive_a(n-b), 1 + recursive_a(n-c)))


def time_a(n):
    start = process_time()
    recursive_a(n)
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