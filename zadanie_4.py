import itertools

def get_combinations(s, k):
    return [''.join(c) for i in range(1, k+1) for c in itertools.combinations(s, i)]