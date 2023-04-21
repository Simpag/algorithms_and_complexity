# Read input for graph
V = int(input())
E = int(input())
m = int(input())
edges = []
for i in range(E):
    u, v = map(int, input().split())
    edges.append((u, v))

# Create casting problem instance
n = V
s = E
k = m
roles = []
constraints_type_1 = []
constraints_type_2 = []
for i in range(1, n+1):
    roles.append(i)
    adj_vertices = [j for j in range(1, k+1) if (i, j) in edges or (j, i) in edges]
    constraints_type_1.append((len(adj_vertices),) + tuple(adj_vertices))
for u, v in edges:
    constraints_type_2.append((2, u, v))

# Add constraints for p1 and p2
p1 = 1
p2 = 2
constraints_type_1[p1-1] = (1, p1)
constraints_type_1[p2-1] = (1, p2)
for i in range(s):
    roles_in_scene = sorted(set(constraints_type_2[i][1:]))
    if len(roles_in_scene) < 2:
        # If a scene has less than 2 roles, add a dummy role to ensure no monologues
        dummy_role = n+1
        roles.append(dummy_role)
        constraints_type_1.append((k,)+tuple(range(1,k+1)))
        constraints_type_2[i] = (2, roles_in_scene[0], dummy_role)
    elif p1 in roles_in_scene and p2 in roles_in_scene:
        # If p1 and p2 are in the same scene, add a dummy role to ensure they never play against each other
        dummy_role = n+1
        roles.append(dummy_role)
        constraints_type_1.append((k,)+tuple(range(1,k+1)))
        roles_in_scene.remove(p2)
        constraints_type_2[i] = (2, roles_in_scene[0], dummy_role)

# Print casting problem instance
print(n)
print(s)
print(k)
for c in constraints_type_1:
    print(*c)
for c in constraints_type_2:
    print(*c)
