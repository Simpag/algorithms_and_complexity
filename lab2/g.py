import math
from matplotlib import pyplot as plt
import networkx as nx

def parse_input(input_string):
    lines = input_string.strip().split('\n')
    n, s, k = map(int, lines[:3])
    constraints_type_1 = {}
    for role, line in enumerate(lines[3:3+n]):
        parts = list(map(int, line.split()))
        actors = parts[1:]
        constraints_type_1[role+1] = actors
    constraints_type_2 = []
    for line in lines[3+n:]:
        parts = list(map(int, line.split()))
        roles = parts[1:]
        constraints_type_2.append(roles)

    # Extract p1 and p2 from the first constraint of type 1
    p1 = 1
    p2 = 2
    
    return n, s, k, constraints_type_1, constraints_type_2, p1, p2


def graph(n, s, k, constraints_type_1, constraints_type_2, p1, p2):
    # Create a graph
    G = nx.Graph()

    # Add nodes for each role
    for role in range(1, n+1):
        G.add_node(f"R{role}")


    # Add edges for constraints of type 2
    # I.e add an edge between every role that appear in the same scene
    for roles in constraints_type_2:
        for i in range(len(roles)):
            for j in range(i+1, len(roles)):
                G.add_edge(f"R{roles[i]}", f"R{roles[j]}")


    # Set position for nodes
    pos = {}
    for role in range(n):
        pos[f"R{role+1}"] = (-math.cos(role/(n)*2*math.pi), math.sin(role/(n)*2*math.pi))
    

    return G, pos



def run(input_string):
    n, s, k, constraints_type_1, constraints_type_2, p1, p2 = parse_input(input_string)
    G, pos = graph(n, s, k, constraints_type_1, constraints_type_2, p1, p2)
    #print(constraints_type_1)
    #print("\n")
    #print(constraints_type_2)

    # Find the coloring if possible
    colors = nx.greedy_color(G)
    uniqueColors = set(colors.values())

    print(f'Can be colored with {len(uniqueColors)} colors')
    print(f"k: {k}")

    color_list = ["gold", "lightblue", "limegreen", "orange", 'red', 'blue']
    nodes = list(G.nodes())
    node_colors = [0, ] * len(nodes)
    for node in colors:
        i = nodes.index(node)
        node_colors[i] = color_list[colors[node]]

    print(set(node_colors))
    assert(len(nodes) == len(node_colors))


    # Draw graph
    nx.draw(G, pos, node_color=node_colors, with_labels=True, font_weight='bold')
    plt.show()