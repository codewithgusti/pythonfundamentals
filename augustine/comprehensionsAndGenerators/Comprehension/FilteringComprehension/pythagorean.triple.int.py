from math import sqrt

# this will generate all possible pairs
mx = 10
triples = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]

# this will filter out all non-Pythagorean triples

triples = list(filter(lambda triple: triple[2].is_integer(), triples))

# this will make the third number in the tuple an integer

triples = list(map(lambda  triple: triple[:2] + (int(triple[2]),),triples))
print(triples)