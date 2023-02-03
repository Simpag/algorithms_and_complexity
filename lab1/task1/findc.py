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

a = 5
b = 6
c = 7
# Find runtime of about 1
for i in range(50_000,10_000_000, 100):
    print(time_b(i), i) # Seg fault before 1 s is reached