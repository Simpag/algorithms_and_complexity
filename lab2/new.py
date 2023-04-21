V = int(input())
E = int(input())
m = int(input())

# Create graph
scenes = []
edges = []
isolated_vertex = [True,] * V
for _ in range(E):
    u, v = map(int, input().split())
    isolated_vertex[u-1] = False
    isolated_vertex[v-1] = False
    edges.append((u,v) if u < v else (v,u)) # add the in increasing order

# Attach verticies with no edges to some edge
for i, is_isolated in enumerate(isolated_vertex):
   if is_isolated:
       # add an edge to anywhere
       edges.append((2, i+1))

# initialize data of output
r = V+2
p = m+1

# Each edge is a scene, reserve role 1 for p1 (diva 1)
for r1, r2 in edges:
    # now add to scenes
    scenes.append(set([r1+2, r2+2]))

# now we need to append the first diva to the graph
# we do this by creating a scene consisting of diva 1 and random actor
scenes.append(set([1, 3]))
scenes.append(set([2, 3]))

# let every actor play every role except for role 1
roles = [list(range(1,p+1)) for x in range(r)]
roles[0].remove(2)
roles[1].remove(1)


print(r)
print(len(scenes))
print(p)
for item in roles:
    print(len(item), *item)
for item in scenes:
    print(len(item), *item)