from functools import reduce
from operator import mul

def factorial(n) :
    return reduce(mul, range(1,1+n), 1)

fact = factorial(5)
print(fact)

