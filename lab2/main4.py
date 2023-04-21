from collections import defaultdict

# Read input
V = int(input())
E = int(input())
m = int(input())

# Create graph
graph = defaultdict(list)
isolated_vertex = [True,] * V
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    isolated_vertex[u-1] = False
    isolated_vertex[v-1] = False
    #graph[v].append(u)

for i, is_isolated in enumerate(isolated_vertex):
    if is_isolated:
        # add an edge to anywhere
        graph[i+1].append(1)

# Create casting problem instance
roles = [str(i) for i in range(1, V + 1)]
actors = [str(i) for i in range(1, m + 1)]
constraints1 = []
constraints2 = []

# Create fake role for p1 and p2
fake_role = str(V + 1)
roles.append(fake_role)

# Helper function to get the list of colors of the neighbors of a vertex
def get_neighbor_colors(vertex):
    return set(str(colors[v]) for v in graph[vertex] if v in colors)

# Create constraints of type 1
for vertex in range(1, V + 1):
    colors = defaultdict(int)
    for neighbor in graph[vertex]:
        colors[neighbor] = colors.get(neighbor, 0) + 1
    allowed_actors = [actor for actor in actors if actor not in get_neighbor_colors(vertex)]
    if '1' in allowed_actors and '2' not in allowed_actors:
        allowed_actors.append('2')
    elif '2' in allowed_actors and '1' not in allowed_actors:
        allowed_actors.append('1')
    constraints1.append(' '.join([str(len(allowed_actors))] + allowed_actors))

# Create constraints of type 2
for u in range(1, V + 1):
    for v in graph[u]:
        constraints2.append(' '.join(['2' ,str(u), str(v)])) # '3' because there are 3 actors in each scene

constraints2[0] = '3' + constraints2[0][1:] + f' {fake_role}'
constraints1.append(f'{len(actors)} {" ".join(actors)}') # The "fake role" can be played by 1 or 2

# Output casting problem instance
print(V+1)
print(len(constraints2))
print(len(actors))
for c in constraints1:
    print(c)
for c in constraints2:
    print(f'{c}')