n = 5
permutation = []
chosen = [False for i in range(n)]

def add_num_to_permutation():
    if len(permutation) == n:
        print(permutation)
    else:
        for i in range(n):
            if chosen[i]: continue
            chosen[i] = True
            permutation.append(i)
            add_num_to_permutation()
            chosen[i] = False
            permutation.pop()

add_num_to_permutation()
