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

    # Add nodes for each actor
    # for actor in range(1, k+1):
    #     G.add_node(f"A{actor}")

    # Add edges for constraints of type 1
    # I.e add edges between every role that an actor can play
    # for role, actors in constraints_type_1.items():
    #     for actor in actors:
    #         G.add_edge(f"R{role}", f"A{actor}")


    # Add edges for constraints of type 2
    # I.e add an edge between every role that appear in the same scene
    for roles in constraints_type_2:
        for i in range(len(roles)):
            for j in range(i+1, len(roles)):
                G.add_edge(f"R{roles[i]}", f"R{roles[j]}")

    # Add edges for the divas not playing together
    # I.e add an edge between all roles that the divas can play
    # for role in range(1, n+1):
    #     #if role not in constraints_type_1[p1] or role not in constraints_type_1[p2]:
    #     #    G.add_edge(f"R{role}", "Divas")
        
    #     # add an edge between all roles that p1 and p2 can play
    #     if p1 in constraints_type_1[role] and p2 in constraints_type_1[role]:
    #         G.add_edge(f"R{role}", "Divas")

    diva_roles = []
    for role in constraints_type_1:
        if p1 in constraints_type_1[role] or p2 in constraints_type_1[role]:
            diva_roles.append(role)

    # print("Diva roles")
    # print(diva_roles)
    # for roles_in_scene in constraints_type_2:
    #     d = [value for value in diva_roles if value in roles_in_scene]

    #     if len(d) > 1:
    #         for role in d:
    #             G.add_edge(f"R{role}", "Divas")
        

    # Set position for nodes
    # pos = {}
    # for role in range(1, n+1):
    #     pos[f"R{role}"] = (1+role/20*(-1)**role, role)
    # for actor in range(1, k+1):
    #     pos[f"A{actor}"] = (2, actor)
    # pos["Divas"] = (3, 1.5)

    return G#, pos


#input_string = "6\n5\n4\n3 1 3 4\n2 2 3\n2 1 3\n1 2\n4 1 2 3 4\n2 1 4\n3 1 2 6\n3 2 3 5\n3 2 4 6\n3 2 3 6\n2 1 6"
# input_string = """5
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
def run(input_string):
    n, s, k, constraints_type_1, constraints_type_2, p1, p2 = parse_input(input_string)
    G = graph(n, s, k, constraints_type_1, constraints_type_2, p1, p2)
    print(constraints_type_1)
    print("\n")
    print(constraints_type_2)

    # Find the coloring if possible
    # colors = nx.greedy_color(G)
    # uniqueColors = set(colors.values())

    # print(f'Can be colored with {len(uniqueColors)} colors')
    # print(f"k: {k}")

    color_list = ["gold", "lightblue", "limegreen", "orange", 'red', 'blue']
    nodes = list(G.nodes())
    node_colors = [0, ] * len(nodes)
    for node in constraints_type_1:
        i = nodes.index(f'R{node}')
        node_colors[i] = color_list[constraints_type_1[node][0]]

    print(set(node_colors))
    assert(len(nodes) == len(node_colors))


    # Draw graph
    nx.draw(G, node_color=node_colors, with_labels=True, font_weight='bold')
    plt.show()