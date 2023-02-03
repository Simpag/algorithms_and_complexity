import sys
sys.setrecursionlimit(100_000_000)

n = int(input())
k = int(input())
p = float(input())

buffer = [None for i in range(n+1)]
def g(x):
    if x < k:
        return 0.0
    elif x == k:
        return p**k
    elif buffer[x] is not None:
        return buffer[x]
        
    buffer[x] = g(x-1) + p**k * (1-p) * (1 - g(x-k-1))
    return buffer[x]

print(g(n))