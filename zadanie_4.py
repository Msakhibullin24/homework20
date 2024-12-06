import itertools

def permutations(s, n):
    return [''.join(p) for p in itertools.permutations(s, n)]

