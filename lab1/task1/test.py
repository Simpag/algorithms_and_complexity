import sys
from time import process_time
sys.setrecursionlimit(100_000_000)

#n = int(input())
#a = int(input())
#b = int(input())
#c = int(input())

a = 5
b = 6
c = 7

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
    
    return end - start

'''epsilon = 0.5
delta = 0.2
while True:
    print(n, ' ', end='')
    t = time_b(n)
    print(t)
    if delta > t - 1 > -delta:
        print(n)
        break
    elif delta > t - 1:
        n = int(n + n*epsilon)
    elif delta < t-1:
        n = int(n - n*epsilon)

    epsilon *= 0.95'''

for i in range(5000, 50000, 100):
    print(time_b(i), i)