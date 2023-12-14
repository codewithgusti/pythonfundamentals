# The preceding iterator creates a generator object that will run forever.
# You can keep calling it, and it will never stop.

def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


c = counter()
print(next(c))
print(next(c))
