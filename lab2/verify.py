# Read input
n = int(input())
s = int(input())
k = int(input())
constraints1 = [input().split()[1:] for _ in range(n)]
constraints2 = [input().split()[1:] for _ in range(s)]

constraints1 = [tuple(map(int, c)) for c in constraints1]
constraints2 = [tuple(map(int, c)) for c in constraints2]

def verify_input(n, s, k, constraints_1, constraints_2):
    # Check that n, s, and k are integers greater than or equal to 2
    if not isinstance(n, int) or not isinstance(s, int) or not isinstance(k, int) or n < 2 or s < 1 or k < 2:
        return 1
    
    # Check that constraints_1 is a list of n tuples
    if not isinstance(constraints_1, list) or len(constraints_1) != n:
        return 2
    
    # Check that each tuple in constraints_1 contains integers between 1 and k
    for constraint in constraints_1:
        if not isinstance(constraint, tuple) or not all(isinstance(actor, int) and 1 <= actor <= k for actor in constraint):
            return 3
    
    # Check that constraints_2 is a list of s tuples
    if not isinstance(constraints_2, list) or len(constraints_2) != s:
        return 4
    
    # Check that each tuple in constraints_2 contains integers between 1 and n
    for constraint in constraints_2:
        if not isinstance(constraint, tuple) or not all(isinstance(role, int) and 1 <= role <= n for role in constraint):
            return 5
    
    return True


print(verify_input(n, s, k, constraints1, constraints2))