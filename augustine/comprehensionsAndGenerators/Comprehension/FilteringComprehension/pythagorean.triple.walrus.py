from math import sqrt

# this is the same step
maximum = 10
# we can combine generating and filtering in one comprehension

triples = [(a,b,int(c)) for a in range(1,maximum) for b in range(a,maximum) if (c:=sqrt(a**2 + b**2)).is_integer()]
print(triples)
