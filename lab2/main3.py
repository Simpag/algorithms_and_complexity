from g import run

# Gather input
V = int(input())
E = int(input())
m = int(input())

edges = []

for i in range(E):
    l = input()
    e = tuple(map(int, l.split(" ")))
    edges.append(e)
    
# Assign number of actors
num_actors = m
actors = list(range(1,num_actors+1))

# Assign number of roles
num_roles = V

# Map edges
# Key: starting point, value endpoints
m_edges = {}
for edge in edges:
    # Color from low to high edge number
    if edge[0] < edge[1]:
        i = 0
        j = 1
    else:
        i = 1
        j = 0

    if edge[i] in m_edges:
        m_edges[edge[i]].append(edge[j])
    else:
        m_edges[edge[i]] = [edge[j],]


# Add colors to verticies, assign same color to the divas
#constraint_1 = [list(range(1,num_actors+1)), ]*num_roles

# All roles can be played by every actor
constraint_1 = [list(range(1,num_actors+1)) for x in range(num_roles)]



# constraint_1 = [list(range(1,num_actors+1)),] * num_roles
# constraint_1[0] = [2,] # second diva gets role 1 (index 0)
# # All roles connected with role 1 cannot be the first diva
# for end in m_edges[1]:
#     constraint_1[end-1] = list(range(2,num_actors+1))

# constraint_1 = [None, ] * num_roles
# actor = 1
# for role in range(1,num_roles+1):
#     if constraint_1[role-1] is None:
#         constraint_1[role-1] = actor
#         actor = actor+1
#         if actor > num_actors:
#             actor = 1
    
#     if role not in m_edges:
#         continue

#     for end in m_edges[role]:
#         if constraint_1[end-1] is None:
#             constraint_1[end-1] = actor
#             actor = actor+1
#             if actor > num_actors:
#                 actor = 1


constraint_2 = []
for x in edges:
    # if x[0] < x[1]:
    constraint_2.append(f'2 {x[0]} {x[1]}')
    # else:
    #     constraint_2.append(f'2 {x[1]} {x[2]}')


# Add another role and assign it the 2nd diva (add one vertex)
num_roles += 1
constraint_1.append([2])
# Connect that role into a scene with the first role
# Make sure that diva 1 cannot play the first role
constraint_1[0].remove(1)
constraint_2.append(f'2 1 {num_roles}')


input_string = ""
input_string += str(len(constraint_1)) + '\n' # number of roles
input_string += str(len(constraint_2)) + '\n' # number of scenes
input_string += str(num_actors) + '\n'
for c in constraint_1:
    a = str(c).replace('[','').replace(']','').replace(',','')
    input_string += str(f'{len(c)} {a}\n')
for c in constraint_2:
    input_string += str(c) + '\n'
input_string = input_string.strip()
print(input_string)


#run(input_string)