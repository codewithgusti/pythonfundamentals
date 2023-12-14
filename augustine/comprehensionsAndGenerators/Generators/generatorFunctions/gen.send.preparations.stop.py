# The preceding iterator creates a generator object that will run forever.
# You can keep calling it, and it will never stop.

# But what if you wanted to stop it at some point?
# One solution is to use a variable to control the while loop,
# as in something such as this


stop = False
def counter(start=0):
    n = start
    while not stop:
        yield n
        n += 1

c = counter()
print(next(c))
print(next(c))
stop = True
print(next(c))
