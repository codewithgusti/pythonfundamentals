# Using Itertools module

from itertools import count

for n in count(5,3):
    if n > 30:
        break
    print(n, end=' ,')