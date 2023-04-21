# Check special cases
# V = 0, V < 2
# E = 0 (no scenes)
# m < 2

def run():
    negative_output = """5
    5
    3
    3 1 2 3
    2 2 3
    2 1 3
    1 2
    3 1 2 3
    2 1 2
    2 1 2
    3 1 3 4
    2 3 5
    3 2 3 5"""

    V = int(input())
    E = int(input())
    m = int(input())

    # Create graph
    scenes = []
    edges = []
    isolated_vertex = [True,] * V # Keep track of all isolated verticies
    for _ in range(E):
        u, v = map(int, input().split())
        isolated_vertex[u-1] = False
        isolated_vertex[v-1] = False
        edges.append((u,v) if u < v else (v,u)) # add the in increasing order

    for i, is_isolated in enumerate(isolated_vertex):
        if is_isolated:
            # add an edge to anywhere
            edges.append((3, i+1))

    # Minimum requirements for a possible solution
    if m < 3 or V < 3 or E < 2:
        print(negative_output)
        return

    # Add one role and one actor to the problem to account
    # for the divas
    n = V+1
    k = m+1

    # Each edge is a scene, add one to avoid using role 1
    for r_1, r_2 in edges:
        # now add to scenes
        scenes.append(set([r_1+1, r_2+1]))

    # Create a scene for the divas
    # Diva 1 and Diva 2 can not play together
    scenes.append(set([1, 3]))

    # Every actor can play every role except for role 1
    # Role 1 is reserved for Diva 1
    roles = [list(range(1,k+1)) for x in range(n)]
    roles[0] = [1]


    print(n)
    print(len(scenes))
    print(k)
    for item in roles:
        print(len(item), *item) # * unpacks the items in the list (might be called spread operator?)
    for item in scenes:
        print(len(item), *item)
        
run()