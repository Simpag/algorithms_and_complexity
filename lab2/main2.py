from g import run

V = int(input())
E = int(input())
m = int(input())

edges = []

for i in range(E):
    l = input()
    e = tuple(map(int, l.split(" ")))
    edges.append(e)
    

actors = list(range(1,m+1))
num_actors = m

num_roles = V # add two diva roles

# available actors for each role will be 1,..,num_actors
constraint_1 = [list(range(1,num_actors+1)) for x in range(num_roles)] # dont include divas
constraint_1[0].remove(1)
constraint_1[1].remove(2)

constraint_2 = []
for x in edges:
    if x[0] < x[1]:
        constraint_2.append(f'2 {x[0]} {x[1]}')
    else:
        constraint_2.append(f'2 {x[1]} {x[2]}')

# add divas
#print(constraint_2)
#for i in range(len(constraint_2)):
#    constraint_2[i] += f' {V+(i%2+1)}'

input_string = ""
input_string += str(num_roles) + '\n'
input_string += str(len(constraint_2)) + '\n' # number of scenes
input_string += str(num_actors) + '\n'
for c in constraint_1:
    a = str(c).replace('[','').replace(']','').replace(',','')
    input_string += str(f'{len(c)} {a}\n')
for c in constraint_2:
    input_string += str(c) + '\n'
input_string = input_string.strip()
print(input_string)


run(input_string)