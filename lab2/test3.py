import networkx as nx
import matplotlib.pyplot as plt

# input
f = """6 
5 
4
3 1 3 4
2 2 3
2 1 3
1 2
4 1 2 3 4
2 1 4
3 1 2 6
3 2 3 5
3 2 4 6
3 2 3 6
2 1 6"""
# f  = """5 
# 5
# 3
# 3 1 2 3
# 2 2 3
# 2 1 3
# 1 2
# 3 1 2 3
# 2 1 2
# 2 1 2
# 3 1 3 4
# 2 3 5
# 3 2 3 5"""

f2 = f.split('\n')
f2 = [x.strip() for x in f2]

# Parse input
n = int(f2[0]) # number of roles
s = int(f2[1]) # number of scenes
k = int(f2[2]) # number of actors

roles = [[0 for y in range(k)] for x in range(n)]
scenes = [[0 for y in range(n)] for x in range(s)]

"""
Here, n is the number of roles, s is the number of scenes, 
k is the number of actors, roles is an n x k matrix where roles[i][j] is 1 if actor j can play role i and 0 otherwise, 
and scenes is an s x n matrix where scenes[i][j] is 1 if role j appears in scene i and 0 otherwise.
"""

def parse_input(input_string):
    lines = input_string.strip().split('\n')
    lines = lines[3:]

    # Create the roles matrix
    for i in range(n):
        line = list(map(int, lines[i].split()))[1:]
        for actor in line:
            roles[i][actor-1] = 1

    # Create the scenes matrix
    for i in range(n, n+s):
        line = list(map(int, lines[i].split()))[1:]
        for role in line:
            scenes[i-n][role-1] = 1

    return roles, scenes


roles, scenes = parse_input(f)

def create_graph():
    pass
