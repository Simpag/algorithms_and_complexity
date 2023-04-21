from matplotlib import pyplot as plt
import networkx as nx

# remove the role edges

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

f = f.split('\n')
f = [x.strip() for x in f]

# Parse input
n = int(f[0]) # number of roles
s = int(f[1]) # number of scenes
k = int(f[2]) # number of actors

roles = []
scenes = []
numberRolesInScene = []

for i in range(n):
    l = f[i+3]
    l = l.split(" ")
    l = [int(x) for x in l]
    roles.append(l[1:])

for i in range(s):
    l = f[i+3+n]
    l = l.split(" ")
    l = [int(x) for x in l]
    scenes.append(l[1:])
    numberRolesInScene.append(l[0])

## Create nodes

# One node for each role in all scenes
totalSceneVerticies = sum([len(roles) for roles in scenes])

# One node for each actor
totalActorVerticies = k

nodes = list(range(1, totalSceneVerticies+totalActorVerticies+1)) # Labeled 1 to Total


## Create edges
edges = []

start = 1 # We first have all of the "Scene Verticies" then "Role Verticies" and lastly "Actor Verticies"
# Edges from roles in scenes to actors that can play the role
for scene in scenes:
    for role in scene:
        for actor in roles[role-1]:
            end = totalSceneVerticies + actor
            edge = (start,end)
            edges.append(edge)
        start += 1


# Add the last "diva edge" from actor 1 to 2
edges.append((totalSceneVerticies + 1, totalSceneVerticies + 2))

# The reduction is now V = len(nodes), E = len(edges), m = k and then all elements of edges
network = nx.DiGraph()

network.add_nodes_from(nodes)
print(f"This network has now {network.number_of_nodes()} verticies.")

network.add_edges_from(edges)
print(f"This network has now {network.number_of_edges()} edges.")



# Find the coloring if possible
#colors = nx.greedy_color(network)
#uniqueColors = set(colors.values())

#print(f'Can be colored with {len(uniqueColors)} colors')
#print(f"k: {k}")

# Draw network
pos = {}
colCount = 0
rowCount = 0
rowOffset = 0
count = 0
for node in nodes:
    if node <= totalSceneVerticies:
        pos[node] = (colCount, rowCount+rowOffset)

        if colCount < numberRolesInScene[count]-1:
            colCount += 1
            rowOffset += 0.1
        else:
            colCount = 0
            rowCount += 1
            rowOffset = 0
            count += 1
    else:
        pos[node] = (max(numberRolesInScene)+1, node-totalSceneVerticies)

#color_list = ["gold", "lightblue", "limegreen", "lightorange"]
#print(colors)
#node_colors = [0,] * len(nodes)
#for node in colors:
#    node_colors[node-1] = color_list[colors[node]]


nx.draw_networkx(network, pos, with_labels=True) #node_color=node_colors,
ax = plt.gca()
ax.margins(0.20)
ax.invert_yaxis()
plt.axis("off")
plt.show()