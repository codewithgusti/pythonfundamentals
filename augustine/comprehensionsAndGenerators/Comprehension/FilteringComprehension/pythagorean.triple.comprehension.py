from math import sqrt

# this is the same step as before
mx = 10
triples = [(a, b, sqrt(a ** 2 + b ** 2)) for a in range(1, mx) for b in range(a, mx)]

# here we combine filter and map in one CLEAN list comprehension
triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]
print(triples)