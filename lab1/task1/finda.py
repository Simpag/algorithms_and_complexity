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

a = 5
b = 6
c = 7
# Find runtime of about 1
for i in range(1,10_000, 1):
    print(time_a(i), i)