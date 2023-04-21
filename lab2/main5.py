from collections import defaultdict

# Read input
V = int(input())
E = int(input())
m = int(input())

# Create graph
edges = []
isolated_vertex = [True,] * V
for _ in range(E):
    u, v = map(int, input().split())
    isolated_vertex[u-1] = False
    isolated_vertex[v-1] = False
    edges.append((u,v) if u < v else (v,u)) # add the in increasing order

for i, is_isolated in enumerate(isolated_vertex):
   if is_isolated:
       # add an edge to anywhere
       edges.append((1, i+1))

# Create casting problem instance
roles = [i for i in range(1, V + 1)]
actors = [i for i in range(1, m + 1)]
constraints1 = [list(range(1,len(actors)+1)) for x in roles] # Actors that can play role i
scenes = [] # Roles in scene i

# Create the scenes
for u,v in edges:
    scenes.append(f'2 {u} {v}')

# Create the constraints
# Assign p1 to r1
constraints1[0] = [actors[0]]
# Find a role that is not connected to r1
is_connected = [False,] * len(roles)
for u, v in edges:
    if u == roles[0] or v == roles[0]:
        is_connected[u-1] = True
        is_connected[v-1] = True

# Assign p2 to that role
for i, is_con in enumerate(is_connected):
    if not is_con:
        constraints1[i] = [actors[1]]
        break

# Output casting problem instance
print(len(roles))
print(len(scenes))
print(len(actors))
for c in constraints1:
    c = list(map(str, c))
    print(f'{len(c)} ' + ' '.join(c))
for c in scenes:
    print(c)