
# input
n = 4
c = (2,2,3,2)       # the number of kWh of electricity you consumed this day
p = (2,5,8,10)      # the variable price per kWh, what you would pay this day if you have no fixed plan.
q = (4,3,4,4)       # the price per kWh for a 1-year plan started this day.
r = (10,9,8,7)      # the price per kWh for a 2-year plan started this day. 
s = (10,10,10,10)   # the price per kWh for a 5-year plan started this day.

def P(x):
    global n, memo
    n = x
    memo = {}
    return p1(0)

def p1(d):
    if d > n:
        return 10**100
    elif d == n:
        return 0

    if d in memo:
        return memo[d]

    q1 = 365 if n-d > 365 else n-d
    r1 = 730 if n-d > 730 else n-d
    s1 = 1825 if n-d > 1825 else n-d

    result = min(c[d]*p[d] + p1(d+1), sum(c[d:d+q1])*q[d] + p1(d+q1), sum(c[d:d+r1])*r[d] + p1(d+r1), sum(c[d:d+s1])*s[d] + p1(d+s1))

    memo[d] = result
    return result


def fake_data(n):
    global c,p,q,r,s
    c = [2,]*n       # the number of kWh of electricity you consumed this day
    p = [2,]*n      # the variable price per kWh, what you would pay this day if you have no fixed plan.
    q = [2,]*n       # the price per kWh for a 1-year plan started this day.
    r = [2,]*n      # the price per kWh for a 2-year plan started this day. 
    s = [2,]*n   # the price per kWh for a 5-year plan started this day.

def time_p(n):
    from time import process_time
    import sys
    sys.setrecursionlimit(100_000_000)
    
    fake_data(n)
    start = process_time()
    P(n)
    end = process_time()

    print(f'Time: {end-start}, {n}')
    
    return end - start

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(100, 19000, 250)
res = [time_p(int(x)) for x in t]
res2 = [(int(x)**1.8)/(5*10**7) for x in t]

plt.title("Runtime")
plt.plot(t, res, label="sim")
plt.plot(t, res2, label="n^1.8")
plt.xlabel(r'n')
plt.ylabel(r'time [s]')
plt.grid()
plt.legend()
plt.savefig('test.png')
plt.close()
