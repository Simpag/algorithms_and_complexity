# Parse input
n = int(input()) # number of roles
s = int(input()) # number of scenes
k = int(input()) # number of actors

p1 = 1 # diva 1
p2 = 2 # diva 2

constraints_type_1 = {}
constraints_type_2 = []

for role in range(n):
    l = input()
    parts = list(map(int, l.split(" ")))
    actors = parts[1:]
    constraints_type_1[role+1] = actors

for i in range(s):
    l = input()
    parts = list(map(int, l.split(" ")))
    roles = parts[1:]
    constraints_type_2.append(roles)


## Create graph
def graph(n, s, k, constraints_type_1, constraints_type_2):
    # Create a graph
    nodes = []
    edges = []

    # Add nodes for each role
    for role in range(1, n+1):
        nodes.append(role)

    # Add nodes for each actor
    for actor in range(1, k+1):
        nodes.append(actor+n)

    # Add one node for the divas
    nodes.append(k+n+1)

    # Add edges for constraints of type 1
    # I.e add edges between every role that an actor can play
    for role, actors in constraints_type_1.items():
        for actor in actors:
            edges.append((role, actor+n))


    # Add edges for constraints of type 2
    # I.e add an edge between every role that appear in the same scene
    for roles in constraints_type_2:
        for i in range(len(roles)):
            for j in range(i+1, len(roles)):
                edges.append((roles[i], roles[j]))



    # Add edges for the divas not playing together
    # I.e add an edge between all roles that the divas can play
    diva_roles = []
    for role in constraints_type_1:
        if p1 in constraints_type_1[role] or p2 in constraints_type_1[role]:
            diva_roles.append(role)

    print("Diva roles")
    print(diva_roles)
    for roles_in_scene in constraints_type_2:
        d = [value for value in diva_roles if value in roles_in_scene]

        if len(d) > 1:
            for role in d:
                edges.append((role, k+n+1))
        


    return nodes, edges


nodes, edges = graph(n, s, k, constraints_type_1, constraints_type_2)

# The reduction is now V = len(nodes), E = len(edges), m = k and then all elements of edges
print(len(nodes))
print(len(edges))
print(k)
for edge in edges:
    print(f'{edge[0]} {edge[1]}')