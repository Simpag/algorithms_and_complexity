# Check special cases
# V = 0, V < 2
# E = 0 (no scenes)
# m < 2

from g import run as draw_graph

def run():
    negative_output = """2
    1
    2
    1 1
    1 2
    2 1 2"""

    positive_output = """3
    2
    3
    1 1
    1 2
    1 3
    2 1 3
    2 2 3"""

    V = int(input())
    E = int(input())
    m = int(input())

    # Create graph
    scenes = []
    edges = []
    isolated_vertex = [True,] * V # Keep track of all isolated verticies
    # O(E)
    for _ in range(E):
        u, v = map(int, input().split())
        isolated_vertex[u-1] = False
        isolated_vertex[v-1] = False
        edges.append((u,v) if u < v else (v,u)) # add the in increasing order

    # O(V)
    # Cant have monolouges but adding an isolated vertex to the graph does
    # not affect if it can be colored or not since the isolated vertex can
    # take any of the colors that the vertex in the graph is close to
    for i, is_isolated in enumerate(isolated_vertex):
        if is_isolated:
            # add an edge to anywhere
            edges.append((3, i+1))

    # Add one role and one actor to the problem to account
    # for the divas
    n = V+1
    k = m+1

    # Minimum requirements for a possible solution of the vertex coloring problem
    # Not needed:
    if V == 0 and E == 0 and m == 0:
        print(positive_output)
        return
    
    if m < 2 and E > 0:
        print(negative_output)
        return
    
    # Needed:
    if E == 0 and m > 0:
        print(positive_output)
        return

    # Minimum requirements for a possible solution of the casting problem
    # 3 Roles  (# verticies)
    # 2 Scenes (# edges)
    # 3 Actors (# colors)
    # Not needed:
    if k < 3 or len(edges) < 2 or n < 3:
        print(negative_output)
        return

    # Each edge is a scene, add one to avoid using role 1
    # O(E+c) where c is some constant (all the isolated verticies)
    for r_1, r_2 in edges:
        # now add to scenes
        scenes.append(set([r_1+1, r_2+1]))

    # Create a scene for the divas
    # Diva 1 and Diva 2 can not play together
    scenes.append(set([1, 3]))

    # Every actor can play every role except for role 1
    # Role 1 is reserved for Diva 1
    # O(n)
    roles = [list(range(1,k+1)) for x in range(n)]
    roles[0] = [1]
    # Since diva 1 is connected to play with role 3,
    # role 3 can not be played by diva 2
    roles[2].remove(2)


    output = str(n) + '\n'
    output += str(len(scenes)) + '\n'
    output += str(k)  + '\n'
    for item in roles:
        output += str(len(item)) + ' '
        output += ' '.join(map(str, item))  + '\n'
    for item in scenes:
        output += str(len(item)) + ' '
        output += ' '.join(map(str, item))  + '\n' 

    print(output)
    return output
        
output = run()
draw_graph(output)

# python main.py < input.txt